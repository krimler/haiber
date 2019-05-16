#-------------------------------------------------------#
from entry import Entry
from typing import Dict
from typing import Tuple
import copy
import json
import pprint
import time
import typing
#-------------------------------------------------------#
import ht
import ll
#-------------------------------------------------------# 
class LRU(json.JSONEncoder):
    def __init__(self, max_size:int=0, abs_time:int=0, idle_time:int=0) ->None:
        assert(max_size >= 0)
        self.max_size:int = max_size
        self.ll:int = ll.LL(max_size)
        self.table:Dict = ht.HT()
        self.abs_time:int = abs_time
        self.idle_time:int = idle_time
        self.hits:int = 0
        self.miss:int = 0
        self.idle_miss:int = 0
        self.abs_miss:int = 0
        self.curr_size:int = 0
    #-------------------------------------------------------#
    def set(self, key:str, value:str, abs_time=0, idle_time=0) -> None:
        entry = Entry()
        old_entry = None
        try:
            old_entry = self.table.find(key)
        except KeyError:
            pass
        if old_entry:
            entry = old_entry
            self.ll.remove_middle(entry)
            self.table.remove(key)
        else:
            entry = Entry(key, value, 0, 0)
        curr_time = int(time.time())
        if abs_time > 0 or self.abs_time > 0:
            abs_value = abs_time if abs_time > 0 else self.abs_time
            entry.abs_time = curr_time + abs_value
         
        if idle_time > 0 or self.idle_time > 0:
            idle_value = idle_time if idle_time > 0 else self.idle_time 
            entry.idle_time = curr_time + idle_value
        self.ll.add_rear(entry)
        if self.max_size > 0 and self.ll.size() > self.max_size:
            e = self.ll.remove_front()
            self.table.remove(e.key) 
    
        self.table.add(key, entry)
    #-------------------------------------------------------#
    def get(self, key:str, functional:bool=True) ->str: #functional: pure functional construct, no side effects.!
        curr_time = int(time.time())
        entry = self.table.find(key)
        if not entry or entry.abs_time > 0 or entry.idle_time > 0:
            self.miss += 1
            if not entry:
                return None 
            remove = False
            if entry.abs_time > 0 and entry.abs_time < curr_time:
                self.abs_miss += 1
                remove = True
            if entry.idle_time > 0 and entry.idle_time < curr_time:
                self.idle_miss += 1
                remove = True
            if remove:
                e = self.ll.remove_middle(entry)
                self.table.remove(e.key)
                return None
        if not functional:
            if self.idle_time:
                entry.idle_time = curr_time + self.idle_time
        self.hits += 1
        return entry.data
    #-------------------------------------------------------#        
    def functional_get(self, key:str) ->str:
        return self.get(key, True)
    #-------------------------------------------------------#
    def ttl(self, key:str) ->Tuple[str, int, int]: #value, abs_time, idle_time
        curr_time = int(time.time())
        entry = self.table.find(key)
        if not entry:
            self.miss += 1
            return None, 0, 0
        timeout = False
        if entry.abs_time > 0 and curr_time > entry.abs_time:
            self.abs_miss += 1
            timeout = True
        if entry.idle_time > 0 and curr_time > entry.idle_time:
            self.idle_miss += 1
            tiemout = True
        if not timeout:
            self.hits += 1
        curr_abs_time = entry.abs_time
        if curr_abs_time > 0:
            curr_abs_time -= curr_time
        curr_idle_time  = entry.idle_time
        if curr_idle_time > 0:
             curr_idle_time -= curr_time
        
        return entry.data, curr_abs_time, curr_idle_time
    #-------------------------------------------------------#
    def stats(self) ->  None:
        self.curr_size = self.ll.size()
        js  = json.dumps(self)
        pp = pprint.PrettyPrinter()
        pp.pprint (js)
#-------------------------------------------------------#
class LRUEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, LRU):
            new_dict = copy.deepcopy(obj.__dict__)
            if 'll' in new_dict:
                del new_dict['ll']
            if 'table' in new_dict:
                del new_dict['table']
            return new_dict
        else:
            return json.JSONEncoder.default(self, obj)
#-------------------------------------------------------#        

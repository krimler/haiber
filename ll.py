#-------------------------------------------------------#
from entry import Entry
from functools import lru_cache
import hashlib
import typing
#-------------------------------------------------------#
class LL:
    def __init__(self, max:int=5) -> None:
        self.front:Entry = None
        self.last:Entry = None
        self.count:int = 0
        self.max:int = max
    #-------------------------------------------------------#
    def size(self) -> int:
        return self.count
    #-------------------------------------------------------#
    def add_rear(self, x:Entry) -> None:
        self.count += 1
        if self.count == 1:
            self.front = self.last = x
            return
        self.last.nxt = x
        x.prv = self.last
        self.last = x
    #-------------------------------------------------------#
    def add_front(self, x:Entry) ->None:
        self.count += 1
        if self.count == 1:
            self.front = self.last = x
            return
        x.nxt = self.front
        self.front.prv = x
        self.front = x
    #-------------------------------------------------------#
    def remove_front(self) -> Entry:
        assert(self.count >= 0) 
        if not self.count : #if no elements
            return None
        self.count -= 1
        if not self.count :
            x = self.last
            self.last = self.front = None
            return x
        else:
            x = self.front
            self.front = self.front.nxt
            self.front.prv = None
            return x
    #-------------------------------------------------------#
    def remove_rear(self) -> Entry:
        assert(self.count >= 0)
        if self.count == 0:
            return None
        self.count -= 1
        if not self.count :
            x = self.last
            self.last = self.front = None
            return x
        else:
            x = self.last
            self.last = self.last.prv
            self.last.nxt = None
            return x
    #-------------------------------------------------------#
    def remove_middle(self, x) -> Entry:
        assert(self.count >= 0)
        if self.count == 0:
            return None
        if self.count > 1:
            x.prv.nxt = x.nxt
            x.nxt.prv = x.prv
        return x
    #-------------------------------------------------------#
    def remove_front(self) -> Entry:
        assert(self.count >= 0)
        if self.count == 0:
            return x
        self.count -= 1
        if not self.count :
            x = self.last
            self.last = self.front = None
            return x
        else:
            x = self.front
            self.front = self.front.nxt
            self.front.prv = None
            return x
    #-------------------------------------------------------#
    def pr(self) -> None:
        print(f"contains {self.count} element/s.")
        n = self.front
        while( n):
            print(n.data)
            n = n.nxt

        print("&")
        n = self.last
        while(n):
            print(n.data)
            n = n.prv
        print(f"---------->") 
#-------------------------------------------------------#

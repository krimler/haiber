#-------------------------------------------------------#
from entry import Entry
from typing import Dict
import typing
#-------------------------------------------------------#
class HT:
    def __init__(self):
        self.table:Dict = {}
    #-------------------------------------------------------#
    def add(self, k:str, v:Entry) -> None:
        self.table[k] = v
    #-------------------------------------------------------#
    def remove(self, k:str) -> None:
        try:
            del self.table[k]
        except KeyError:
            pass
    #-------------------------------------------------------#
    def find(self, k:str) -> Entry:
        if k in self.table:
            return self.table[k]
        return None
    #-------------------------------------------------------#
    def pr(self) -> None:
        for each in self.table:
            print(f"{each} : {self.table[each]}")
#-------------------------------------------------------#

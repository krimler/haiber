import typing
class Entry:
    def __init__(self, key:str=None, value:str =None, abs_time:int=0, idle_time:int=0) -> None:
        self.data = value
        self.abs_time = abs_time
        self.idle_time = idle_time
        self.prv = None
        self.nxt = None
        self.key = key
    def __repr__(self) -> str:
        return 'key:' + self.key + '\t' + 'Data:' + str(self.data) + '\t' +\
'absolute time:' + str(self.abs_time) + '\t' +\
'idle time:' + str(self.idle_time) + '\n'

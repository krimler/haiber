from cache import LRU
import time

lru = LRU(10, 6, 3) # max 10 elements, 60 seconds absolute timeout, 30 seconds idle timeout.
lru.set("foo", "bar")
res = lru.get("foo")
print(f"immediately value is {res}")
time.sleep(4)
print(f"after 4 seconds value is {res}")
value, abso, idle = lru.ttl("foo")
print (f"value is {value} with abs_time {abso} and idle time {idle} remaining.")

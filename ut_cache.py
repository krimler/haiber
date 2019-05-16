from cache import LRU

def test_basic():
    lru = LRU()
    lru.set("madhava", "Gaikwad", 5)
    v = lru.ttl("madhava")
    print("madhav---> " + str(v))
    time.sleep(3)
    v = lru.ttl("madhava")
    print("madhav---> 3 sec sleep " + str(v))
    time.sleep(3)
    v = lru.get("madhava")
    print("madhav---> 3 sec sleep " + v)
    print(lru.ttl("madhava"))
    #lru.stats()
    #e = LRUEncoder().encode(lru)
    #print (e)

def test_max():
    lru = LRU(1)
    lru.set("foo", "bar");
    lru.set("foo1", "bar1");
    lru.set("foo2", "bar2");
    v = lru.get("foo1")
    print(v);
    print('{{{{{{{')
    lru.table.pr()

def test_normal():
    lru = LRU()
    lru.set("foo", "bar")
    lru.set("wow", "wow1")
    lru.set("gow", "gow1")
    lru.table.pr()

def test_global_idle():
    lru = LRU(2, 0, 2)
    lru.set("foo1", "bar")
    time.sleep(4)
    lru.table.pr()
    v, t1, t2 = lru.ttl("foo1")
    print(v + str(t1) + str(t2))

def test_idle():
    lru = LRU(2, 0, 0)
    lru.set("foo1", "bar", 0, 2)
    time.sleep(4)
    lru.table.pr()
    v, t1, t2 = lru.ttl("foo1")
    print(v + str(t1) + str(t2))
def test_global_abs():
    lru = LRU(2, 2, 0)
    lru.set("foo1", "bar")
    time.sleep(4)
    lru.table.pr()
    v, t1, t2 = lru.ttl("foo1")
    print(v + str(t1) + str(t2))
def test_abs():
    lru = LRU(2, 0, 0)
    lru.set("foo1", "bar", 2 , 0)
    time.sleep(4)
    lru.table.pr()
    v, t1, t2 = lru.ttl("foo1")
    print(v + str(t1) + str(t2))
#test_basic()
#test_max()
#test_normal()
#test_idle()
#test_global_abs()
#test_abs()

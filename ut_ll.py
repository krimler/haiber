from ll import LL
class Node:
    def __init__(self, x):
        self.prv = None
        self.nxt = None
        self.data = x
        self.abs_time = 0
        self.idle_time = 0

class LRU_LL(LL):
    def __init__(self, max1=5):
        print(f"Got value for max size as{max1}")
        super().__init__(max = max1)
        #super(max1=max)
    def insert(v):

        if self.count == self.max:
            self.remove_front()
            self.add_front(v)
        else:
            self.add_front(v)

def examine_rear():
    ll = LL()
    n = Node(5)
    ll.pr()
    ll.add_rear(n)
    ll.add_rear(Node(7))
    ll.pr()
    ll.remove_rear()
    ll.add_rear(Node(9))
    ll.pr()
    ll.remove_rear()
    ll.pr()

def examine_front():
    ll = LL()
    n = Node(5)
    ll.pr()
    ll.add_front(n)
    ll.add_front(Node(7))
    ll.pr()
    ll.remove_front()
    ll.add_front(Node(9))
    ll.pr()
    ll.remove_front()
    ll.pr()
def examine_rear_front():
    ll = LL()
    n = Node(5)
    ll.pr()
    ll.add_rear(n)
    ll.add_rear(Node(7))
    ll.pr()
    ll.remove_front()
    ll.add_rear(Node(9))
    ll.pr()
    ll.remove_front()
    ll.pr()

def examine_front_rear():
    ll = LL()
    n = Node(5)
    ll.pr()
    ll.add_front(n)
    ll.add_front(Node(7))
    ll.pr()
    ll.remove_rear()
    ll.add_front(Node(9))
    ll.pr()
    ll.remove_rear()
    ll.pr()

#examine_rear()
#examine_front()
#examine_rear_front()
#examine_front_rear()


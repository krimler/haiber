from ht import HT
def examine_ht():
    h = HT()
    h.pr()
    h.add("foo", "bar")
    h.add("wow", "bow")
    h.pr()
    h.remove("goo")
    h.pr()
    h.remove("foo")
    h.add("goo1", "boo")
    h.add("foo1", "bar1")
    print('--------->')
    h.pr()
    h.find('wowowow')

examine_ht()

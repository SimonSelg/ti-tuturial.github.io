class Fruit:
    allinstcnt = 0
    instcnt = 0
    otherallinstcnt = 0

    def __init__(self):
        Fruit.allinstcnt += 1
        self.incr_instcnt()

    @classmethod
    def __str__(cls):
        return "%s: %s" %(cls.__name__, cls.allinstcnt)

    @staticmethod
    def print_allinstcnt():
        print("%d global instances" % Fruit.allinstcnt)

    @classmethod
    def print_instcnt(cls):
        print("%d local instances" % cls.instcnt)

    @classmethod
    def incr_instcnt(cls):
        cls.instcnt += 1

    def incr_oincnt(self):
        Fruit.otherallinstcnt

    def print_oinstcnt(self):
        print(self.otherallinstcnt)


class Cherry(Fruit):
    instcnt = 0

    def __init__(self, **kw):
        super().__init__(**kw)


class SourCherry(Cherry):
    instcnt = 0

    def __init__(self, **kw):
        super().__init__(**kw)

s1 = Cherry(); s2 = Cherry(); s3 = Cherry()
r1 = SourCherry()

print(r1)
print(s1)
print(s3)

Fruit.print_allinstcnt()
Fruit.print_instcnt()

s1.print_allinstcnt()
r1.print_instcnt()
s1.print_instcnt()

s4 = Cherry()
r2 = SourCherry()

r1.print_oinstcnt()
s1.print_oinstcnt()
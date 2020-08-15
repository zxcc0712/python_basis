class A:
    def hello(self):
        print("qqq")

class B(A):
    pass


a = A()
b = B()
a.hello()
b.hello()

#重写是继承机制的一个重要方面
def check_index(key):
    """
    指定的健是否是可接受的索引

    键必须是非负整数，才是可接受的。
    如果不是整数，将引发TypeError异常；
    如果是负数，将引发IndexError异常
    """
    if not isinstance(key,int):raise TypeError
    if key<0:raise IndexError

class ArithmeticSequence:

    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        check_index(key)
        try:return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __set__(self, key, value):
        check_index(key)
        self.changed[key] = value

s = ArithmeticSequence(1,2)
s.__getitem__(9)
print(s[0],s[1],s[2],s[3],s[9])
#多态、封装、集成
#属性
#创建类
# class Person:
#     def set_name(self,name):
#         self.name = name
#     def get_name(self):
#         return self.name
#     def greet(self):
#         print('hello world! I am {}'.format(self.name))
#
# foo = Person()
# foo.set_name('aaaaa')
# foo.greet()
# print(foo.name)

class Bird:
    song = 'pppp'
    def sing(self):
        print(self.song)

bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()

#使用hasattr来监察所需的方法是否存在

#抽象基类

from  abc import ABC,abstractmethod
#抽象类是在子类中必须实现的方法
class Talker(ABC):
    #用#abstractmethod来将方法标记成抽象的
    @abstractmethod
    def talk(self):
        pass

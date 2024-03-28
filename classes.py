# Python3 program to
# demonstrate instantiating
# a class
class Dog:

    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

#Self参数
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company
        def show(self):
            print('Hello my name is '+ self.name+ 'and i work in ' + self.company +'.')
        obj = GFG('Jhon','Geeks')
        obj.show()

class GFG:
    def __init__(somename, name, company):
        somename.name = name
        somename.company = company
        def show(somename):
            print('Hello my name is '+ somename.name + 'and i work in ' + somename.company +'.')
    obj = GFG('Jhon','Geeks')
    obj.show()

# Sample class with init method
class Person:
#__init__方法
    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()

#创建一个person类
class Person:
  def __init__(self, name, age):   #内置函数
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#__str__方法
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company=company
    def __str__(self):
            return f' my name is {self.name} and i work in {self.company}.'
my_obj=GFG('Jhon','Geeks')
print(my_obj)

#返回对象为字符串
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)

print(p1)

#Object方法
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#self参数
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
p1.age=40          #修改对象属性
del p1.age        #删除age属性

#pass语句
class person:
   pass








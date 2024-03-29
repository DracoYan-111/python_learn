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

#Inheritance  继承
#创建父类        Person firstname lastname printname
class Person:
   def __init__(self,fname,lname):
      self.firstname = fname
      self.lastname = lname
   def printname(self):
      print(self.firstname, self.lastname)
      
x = Person('Jhon', 'Due')
x.printname()

#创建子类   Student Person
class Student(Person):
   pass

x = Student('Mike', 'Olsen')
x.printname()

#将函数添加到类 __int__() Student
class Student(Person):
   def __init__(self, fname, lname, year):
      # Person.__init__(self, fname, lname)
      super().__init__(fname, lname)       #自动继承方法和属性
      # self.graduationyear = 2019          #添加属性
      self.graduationyear = year
x = Student('Mike','Olsen', 2019)
#添加一个调用到类的方法  welcome Student
class Student(Person):
   def __init__(self, fname, lname, year):
      super().__init__(fname, lname)       #自动继承方法和属性
      self.graduationyear = year
   def welcome(self):
      print('Welcome', self.firstname, self.lastname, 'to the class of', self.graduationyear)

class Animal:
   def speak(self):
      print('Animal Speaking')
class Dog(Animal):
   def bark(self):
      print('dog barking')      #狗叫
class DogChild(Dog):
   def eat(self):
       print("Eat break...")
d = DogChild()
d.bark()
d.speak()
d.eat()

#多重继承
class Calculation1:     #计算
   def Summation(self,a,b):      #求和
     return a+b;
class Calculation2:
   def Multiplication(self,a,b):   #乘法
      return a*b;
class Derived(Calculation1,Calculation2):
   def Divide(self,a,b):        #除
     return a/b;
d = Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20)) 
#issubclass（sub， sup） 方法用于检查指定类之间的关系(子类，父类)
print(issubclass(Derived, Calculation2))
print(issubclass(Calculation1, Calculation2))
#isinstance（） 方法用于检查对象和类之间的关系
print(isinstance(d,Derived))

#method overriding  方法覆盖
class Bank:
   def getroi(self):
      return 10;
class SBI(Bank):
   def getroi(self):
      return 7;
class ICICI(Bank):
   def getroi(self):
      return 8;
b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:",b1.getroi());     #输出利率
print("SBI Rate of interest:",b2.getroi());
print("ICICI Rate of interest:",b3.getroi());

#Method
class Pet(object):   #先定义Pet类
   def my_method(self):
      print("I am a Cat")      #创建了对象
cat = Pet()
cat.my_method()        #自定义的方法称为。。。


#显示 int 类继承的魔术方法
print(dir(int))

#int方法
# declare our own string class 
class String: 
	
	# magic method to initiate object 
	def __init__(self, string): 
		self.string = string 
		
	# print our string object 
	def __repr__(self): 
		return 'Object: {}'.format(self.string) 
		
	def __add__(self, other): 
		return self.string + other 

# Driver Code 
if __name__ == '__main__': 
	
	# object creation 
	string1 = String('Hello') 

	# print object location 
	print(string1) 
  # concatenate String object and a string 
# print(string1 +' world') 
print(string1 + 'Geeks')

num = 10
res = num.__add__(5)
print(res)

#__new__()
class Employee:
    def __new__(cls):
        print('__new__ magic method is called')
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print('__init__ magic method is called')
        self.name='Satya'
#__str__()
        num = 12
        val = int.__str__(num)
        print(type(val))
#返回对象以字符串形式显示
class employee:
  def __init__(self):
    self.name='Swati'
    self.salary=10000
  def __str__(self):
    return 'name='+self.name+', salary=$'+str(self.salary)
    
    
e1 = employee()
print(e1)
#覆盖__add__()
class distance:
  def __init__(self, x=None,y=None):
    self.ft=x
    self.inch=y
  def __add__(self,x):
    temp=distance()
    temp.ft=self.ft+x.ft
    temp.inch=self.inch+x.inch
    if temp.inch>=12:
        temp.ft+=1
        temp.inch-=12
        return temp
  def __str__(self):
    return 'ft:'+str(self.ft)+' in: '+str(self.inch)
    
    
d1=distance(3,10)
d2=distance(4,4)
print("d1= {} d2={}".format(d1, d2))

d3=d1+d2
print(d3)

#在距离类中添加了以下方法以重载运算符。>=
class distance:
  def __init__(self, x=None,y=None):
      self.ft=x
      self.inch=y
  def __ge__(self, x):
      val1=self.ft*12+self.inch
      val2=x.ft*12+x.inch
      if val1>=val2:
          return True
      else:
          return False
          
          
d1=distance(2,1)
d2=distance(4,10)
print(d1>=d2)



# This is my first lesson in learning Python
# print('Hello Python')
# temperature=35
# if temperature > 30:
#   print("It's a hot day")  
#   print('Drink plenty of water')
# elif temperature >20:
#   print('It\'s a nice day')
# elif temperature >10:
#   print('It\'s a bit day')
# else:
#   print('It\'s a cold')
# print('Done')
#体重转换器
# weight=int(input("Weight: "))
# unit=input("(K)g or (L)bs: ")
# if unit.upper()=="K":
#   converted=weight/ 0.45
#   print("Weight is Lbs: "+ str(converted))
# else:
#   converted=weight*0.45
#   print("Weight is Lbs: " + str(converted))
#循环
i=1
while i >=5:
    print(i * '*')
    i=i+1
names=['John','Bob','Mosh','Som','Mary']
names[0]='Jon'
print(names[0:3])  #索引
#列表
numbers=[1,2,3,4,5]
# numbers.append(6) #新加元素
# numbers.insert(0, -1)                  #在某位置新加元素(在开头)
# numbers.remove(3)          #删除某个元素
# numbers.clear()   #删除列表
# print(1 in numbers) 
# print(len(numbers))   #查看有多少项
 #迭代列表
for item in numbers:
    print(item)
    i=0
    while i <len(numbers):
        print(numbers[i])
        i=i+1
#range函数生成数字序列    给出一个范围
# number1=range(5)
number2=range(5,10,2)   #起始值，终止值，布长
for number in number2:      #迭代范围里的数
  print(number)
#直接调用range
for number in range(5):
  print(number)


#元组  一旦创建不可更改
  #计数，索引
numbers=(1,2,3,3,3)
numbers.count(3)
#conditional statement
def main():
   x,y=8,4
   if(x<y):
      set='x is less than y'
   else:
      set='x is greater than y'
print(set)
# Python program to demonstrate    #隐式
# type Casting 

# int variable
a = 5

# typecast to float
n = float(a)

print(n)
print(type(n))
# Python program to demonstrate 
# type Casting 

# int variable
a = 5

# typecast to int
n = int(a)

print(n)
print(type(n))
# Python program to demonstrate 
# type Casting 

# int variable
a = 5

# typecast to str
n = str(a)

print(n)
print(type(n))
#string variable   字符串变量
a='5'
b='t'
#typecast to int 类型转换为int
n=int(a)
print(n)
print(type(n))

print(str(b))
print(type(b))
#真假值
# number=0
# if number:
#    print(number)
#空列表 []
# 空元组 （）
# 字典 {}
# 空集 set（）
# 空字符串 “ ”
# 空范围范围（0）
#内置bool（）函数
# define a function for checking 
# number is even or odd 
def even_odd(number): 
	
 if number % 2: 
	
	# since num % 2 is equal to 1     奇数
	# which is Truthy Value 
  return 'odd number'
	
 else: 
	
	# since num%2 is equal to 0      偶数
	# which is Falsy Value. 
 	return 'even number'

result1 = even_odd(7) 

# prints odd 
print(result1) 

result2 = even_odd(4) 

# prints even 
print(result2) 

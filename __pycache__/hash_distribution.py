#创建词典
#使用大括号
my_dict={'Dava':'001', 'Ava':'002', 'Joe':'003'}
print(my_dict)
type(my_dict)
#使用dict()函数
new_dict=dict()   #创建一个空字典
print(new_dict)
type(new_dict)
#嵌套词典
emp_details = {'Employee':{'Dava': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation':'Python Developer'},
                            'Ava': {'ID':'002',
                                    'Salary':2300,
                                    'Designation': 'Java Developer'},
                           'Joe':{'ID':'003',
                                  'Salary': 2600,
                                  'Designation':'Python Developer'}}}
#访问值
my_dict={'Dava':'001', 'Ava':'002', 'Joe':'003'}
my_dict['Dava']   #使用键值
print(my_dict.keys()) #使用函数
print(my_dict.values())
print(my_dict.get('Dava'))
print("all keys")                       #实现for循环
for x in my_dict:
    print(x)          #print keys
print("all values")                       
for x in my_dict.values:
    print(x)         #print values
print("all keys and values")
for x,y in my_dict.items():
    print(x,':' ,y)
#更新值
my_dict={'Dava':'001', 'Ava':'002', 'Joe':'003'}  
my_dict['Dava'] = '004'
my_dict['Chris'] = '005'
print(my_dict)
#从字典中删除项目
my_dict = {'Dava': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
del my_dict['Dava']
my_dict.pop('Ava')
my_dict.popitem()         #移除最后一个项目
print(my_dict)
#将字典转化为数据帧、
import pandas as pd
emp_details = {'Employee':{'Dava': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation':'Python Developer'},
                            'Ava': {'ID':'002',
                                    'Salary':2300,
                                    'Designation': 'Java Developer'},
                           'Joe':{'ID':'003',
                                  'Salary': 2600,
                                  'Designation':'Python Developer'}}}
df = pd.DataFrame(emp_details['Employee'])
print(df)
#哈希表
import string
text = string.ascii_uppercase * 100_000_000

text[:50]  # Show the first 50 characters

len(text)
text[0]  # The first element
text[len(text) // 2]  # The middle element
text[-1]  # The last element, same as text[len(text) - 1]
#哈希值是不可变的
hash('Loerm')
hash('Loerm')
hash('Loerm')
hash(3.14)
hash([1, 2, 3])
# hash_distribution.py
# 哈希值的直方图
from collections import Counter

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")
from hash_distribution import plot, distribute
from string import printable

plot(distribute(printable, num_containers=2))
plot(distribute(printable, num_containers=5))
id('Lorem')
#制作自己的哈希表
def hash_function(text):
 return sum(ord(character) for character in text)
def hash_function(key):
  return sum(ord(character) for character in str(key))

hash_function("Lorem")
hash_function(3.14)
hash_function(True)
def hash_function(key):
   return sum(ord(character) for character in repr(key))

hash_function("3.14")
hash_function(3.14)
def hash_function(key):
  return sum(
      index * ord(character)
                for index, character in enumerate(repr(key), start=1)
   )
hash_function("Tiny")
hash_function("This has a somewhat medium length.")
hash_function("This is very long and slow!" * 1_000_000)
hash_function("Tiny") % 100
hash_function("This has a somewhat medium length.") % 100
hash_function("This is very long and slow!" * 1_000_000) % 100

from hash_distribution import plot, distribute
from string import printable

plot(distribute(printable, 6, hash_function))

hash_function("a"), hash_function("b"), hash_function("c")
(350, 352, 354)

def hash_function(key):
     return sum(
           index * ord(character)
       for index, character in enumerate(repr(key).lstrip("'"), 1)
   )
hash_function("a"), hash_function("b"), hash_function("c")
plot(distribute(printable, 6, hash_function))
# 了解您的 Python 解释器正在使用哪种哈希算法
import sys
sys.hash_info.algorithm




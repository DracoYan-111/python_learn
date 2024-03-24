#元组
color1='blue'
color2='green'
color3='red'
color4='yellow'
# print(color1,color2,color3,color4)
color=['blue','green','red','yellow']
print(color[0],color[1],color[2],color[3])

names_1=['John','Anny','Jacob','Olivia']     #列表   (可变)
names_t=('John','Anny','Jacob','Olivia')       #元组
print(type(names_1))
print(type(names_t))

empty_tuple=()
print(empty_tuple)    #空元组输出()
#整数元组
integer_tuple=(1,2,3)
print(integer_tuple)
#混合数据类型
mixed_tuple=(0,'Hello',1.2,'World')
print(mixed_tuple)
#嵌套元组
nested_tuple=('aardvark',[0,1,2],(2,1,0))
print(nested_tuple)
#访问元组 
tns_tuple=('N','e','w','a','s','d','t','s','r','s')    #基本元组
print(tns_tuple[0])
n_tuple=('kjnbh','gfdx',[2,3,4,5,6,7])        #嵌套元组
print(n_tuple[0][3])                         #打印元组0中的第三个元素
#使用切片访问元素
tns_tuple=('N','e','w','a','s','d','t','s','r','s')
print(tns_tuple[0:3])                           #打印前三个元素
print(tns_tuple[1:6])              #打印后五个元素
#可以对元组使用串联和重复
print(('T','h','e')+('N','e','w')+('S','t','a','c','k'))
#对*运算符重复使用
print(('The New Stack',)*3)
#项目进行计数和索引
tns_tuple=('N','e','w','a','s','d','t','s','r','s')
print(tns_tuple.count('s'))   #对s进行计数
print(tns_tuple.index('s'))    #对s位置进行第一次索引
i=tns_tuple.index('s')
tns_tuple.index('s',i+1)

import pandas as pd
colors=['blue','green','red','yellow']
fruits=['blueberry','apple','cherry','banana']
print(colors[0],fruits[0],colors[1],fruits[1],colors[2],fruits[2],colors[3],fruits[3])
df=pd.DataFrame(columns=['colors','fruits'])
df['colors'],df['fruits']=colors,fruits
print(df)

#set集  元素是唯一的
set_exmple={1,1,2,3,4,4,4}
print(set_exmple)

#tuple list set dic
#list
l=[]
#Adding element into list
l.append(5)
l.append(10)
print('Adding 5 and 10 in list',l)
#Popping Elements from list     从列表中弹出元素
l.pop()
print('Popping one element from list',l)
print()
#set
s=set()
#Adding element into set
s.add(5)
s.add(10)
print('Adding 5 and 10 in set',s)
#Remove element from set
s.remove(5)
print('Removing 5 from set',s)
print()
#Tuple
t=tuple(l)
#Tuples are immutable     元组是不可变的
print('Tuple',t)
print()
#dictionary
d={}
#Adding the key value pair     增加键值对
d[5]='five'
d[10]='ten'
print('Dictionary',d)
#Remove key_value pair
del d[10]
print('dictionary',d)

#正则表达式
normal='Hello\nWorld'
print(normal)
raw=r'Hello\nWWorld'        #原始字符串运算符“r”，转义字符的效果不会按照其含义进行转换
print(raw)

import re
str='an example word:cat!!'
match=re.search(r'world:\w\w\w',str)
if match:
    print('found',match.group())
else:
    print('did not find')
#你怎么称呼三只眼睛的猪
  ## Search for pattern 'iii' in string 'piiig'.
  ## All of the pattern must match, but it may appear anywhere.
  ## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
match = re.search(r'igs', 'piiig') # not found, match == None

  ## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

  ## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"

#电子邮件示例
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print(match.group())  ## 'b@google'
#方括号
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group())  ## 'alice-b@google.com'









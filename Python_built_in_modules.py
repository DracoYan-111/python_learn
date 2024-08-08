#操作系统模块
#使用 os 模块中的 mkdir（） 函数创建一个新目录
# import os
# os.mkdir("D:\myCode\Python\\tempdir")    #创建了 tempdir 文件夹
# #更改当前工作目录以使用 chdir（） 函数
# import os
# os.chdir("D:\myCode\Python\\chdir")
# #getcwd（）：此函数返回当前工作目录的名称
# os.getcwd()
# "D:\myCode\Python\\temp"
#os 模块中的 rmdir（） 函数删除具有绝对路径或相对路径的指定目录。但是，它不应该是当前工作目录，它应该是空的

import os
# os.mkdir("D:\myCode\Python\\tempdir")
# os.chdir("D:\myCode\Python\\tempdir")
os.getcwd()
os.chdir("..")
os.rmdir("temp")
#os 模块具有 listdir（） 函数，它返回指定目录中所有文件的列表
import os
os.listdir("c:\\Users")


#随机模块

import random
random.random()        #随机浮点数
random.randint(1,100)   #随机整数
#随机.randrange（）：
#从 start、stop 和 step 参数创建的范围内返回一个随机元素。
#start 、 stop 和 step 参数的行为类似于 range（） 函数。
random.randrange(1,10)
random.randrange(1,10,2)
random.randrange(0,101,10)
#随机.choice（）：从序列对象（如字符串、列表或元组）返回随机选择的元素。空序列 as 参数引发 IndexError
import random
random.choice('computer')
random.choice([1,2,3,4,5])
random.choice((2,3,4,5,6))
#随机.shuffle（）：此函数随机对列表中的元素进行重新排序
numbers=[12,23,45,67,65,43]
random.shuffle(numbers)
numbers
#数学模块
import math
math.pi
math.e
#三角函数
math.radians(30)   #将角度（以度为单位）转换为弧度
math.degrees(math.pi/6)   #将角度（以弧度为单位）转换为度数
math.sin(0.5235987755982988)
math.cos(0.5235987755982988)
math.tan(0.5235987755982988)
math.log10(10)
math.log()
math.e**10   #exp（x） 等价于 e**x
#数学.pow（）：此函数接收两个浮点参数，从第一个增加到第二个并返回结果
math.pow(4,4)
4**4
math.sqrt(100)     #算术平方根
math.sqrt(3)
math.ceil(2.4567)   #将给定的数字近似为大于或等于给定浮点数的最小整数
math.floor(2.4567)    #返回小于或等于给定数字的最大整数

#sys模块
import sys          #此返回传递给 Python 脚本的命令行参数列表
print("My name is {}.I am {} years old".format(sys.argv[1],sys.argv[2])) 
sys.exit
sys.maxsize                         #返回变量可以采用的最大整数
sys.path          #用于返回所有 Python 模块的搜索路径
#标准输入、输出和错误的文件对象
sys.stdin
sys.stdout    
sys.stderr                  
sys.version   #此属性显示一个字符串，其中包含当前 Python 解释器的版本号

#集合模块
import collections
# employee=collections.namedtuple('employee', [name, age, salary])   #姓名年龄薪水
# e1=employee("Ravi",251, 20000)

#OrderedDict()函数    有序词典类似于普通词典
d1={}
d1['A']=20
d1['B']=30
d1['c']=40
d1['D']=50
for k,v in d1.items():
    print(k,v)

import collections
d2=collections.OrderedDict()
d2['A']=20
d2['B']=30
d2['c']=40
d2['D']=50
for k,v in d2.items():
    print(k,v)
#deque 对象支持从列表的两端进行追加和弹出操作
q=collections.deque([10,20,30,40])
q.appendleft(110)     #左插入
q
q.append(41)       #右端插入
q
q.pop()       #最后一个数
q.popleft()   #最左边数

#统计模块
import statistics
statistics.mean([2,5,6,9])   #计算算数平均值
statistics.median([2,5,6,9]) #中位数
statistics.mode([2,3,4,3,3,2,2,2])   #众数
statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5])   #标准偏差

#时间模块
import time
time.time()
tk=time.time()
tp=time.localtime(tk)
time.asctime(tp)    #可读
time.ctime() #此函数返回系统当前时间的字符串表示形式
time.sleep(20)     #睡眠
time.ctime()

from example import some_function

#import standard math module 
import math

# use math.pi to get value of pi
print("The value of pi is", math.pi)










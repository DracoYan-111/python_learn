#数组
#创建方法1
import array as arr
numbers = arr.array('i',[10,20,30])   #整数型
numbers = arr.array('i',[10.0,20,30])   #存在浮点数
print(numbers)
print(len(numbers))
print(numbers[0])   #正索引
print(numbers[1])
print(numbers[2])
print(numbers[-1])   #负索引
print(numbers[-2])
print(numbers[-3])
print(numbers.index(10))    #搜索元素
for number in numbers:
    print(number)       #遍历
print(numbers[:2])
print(numbers[1:3])     #左闭右开
numbers[0] = 40    #更改
print(numbers)
numbers.append(40)      #添加一个
print(numbers)
numbers.extend([50,60,70])         #添加多个
print(numbers)
numbers.insert(0,80)         #特定位置添加新值
print(numbers)
numbers.remove(40)          #删除元素
print(numbers)
numbers.pop(3)          #删除特定位置的元素
print(numbers)

#或者使用函数
for value in range(len(numbers)):
    print(numbers[value])


#创建方法2
from array import *
numbers = array('d',[10.0,20.0,30.0])   #浮点型
print(numbers)
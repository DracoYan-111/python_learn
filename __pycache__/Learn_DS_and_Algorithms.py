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
print(numbers[:2])      #切片
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

#切片数组
import array as arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
	print(i, end=" ")
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)
Sliced_array = a[5:]
print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_array)
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)

#对数组的元素进行计数
import array
my_array = array.array('i', [1, 2, 3, 4, 2, 5, 2])
count = my_array.count(2)
print("Number of occurrences of 2:", count)        #有几个2

#反转数组中的元素
import array
my_array = array.array('i',[1,2,3,4,5])
print('Original array:', *my_array)
my_array.reverse()
print('Reverse array:', *my_array)


#创建链表
from collections import deque
deque('abc')
deque(['a', 'b', 'c'])
deque([{'data':'a'},{'data':'b'}])

llist = deque('abcde')  #创建对象
llist

llist.append('f')   #右侧增加元素
llist
llist.pop()                    #删除右侧元素

llist.appendleft('z')   #左侧增加元素
llist
llist.popleft()                    #删除左侧元素


#创建方法2
from array import *
numbers = array('d',[10.0,20.0,30.0])   #浮点型
print(numbers)

#创建队列
from collections import deque
queue = deque()
queue
deque([])

queue.append("Mary")
queue.append("John")
queue.append("Susan")
queue
deque(['Mary', 'John', 'Susan'])
#第一个进入第一个出
queue.popleft()
queue

queue.popleft()
queue

#创建链表
class LinkedList:         #创建一个类表示列表
    def __init__(self):
        self.head = None
    def __repr__(self):
         node = self.head
         nodes = []
         while node is not None:
              nodes.append(node.data)
              node = node.next
         nodes.append("None")
         return '->'.join(nodes) 

class Node:               #创建一个类表示链的每个节点
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
         return self.data
    
llist = LinkedList()
llist


first_node = Node("a")
llist.head = first_node
llist


second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
llist

#遍历

def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = node.next

llist = LinkedList(["a", "b", "c", "d", "e"])
llist

for node in llist:
   print(node)

#开头插入新节点
def add_first(self, node):
    node.next = self.head
    self.head = node
llist = LinkedList()
llist

llist.add_first(Node('b'))
llist
llist.add_first(Node('a'))
llist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

llist = LinkedList()
llist

llist.add_first(Node('b'))
llist
llist.add_first(Node('a'))
llist

#高级链表
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
#循环列表
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))
circular_llist = CircularLinkedList()
circular_llist.print_list()

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
d.next = a
circular_llist.head = a
circular_llist.print_list()

circular_llist.print_list(b)
circular_llist.print_list(d)






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

#创建堆栈
class Stack:
 def __init__(self):
    self.items = []

 def isEmpty(self):
    return self.items == []

 def push(self, item):
    self.items.append(item)

 def pop(self):
    return self.items.pop()

 def peek(self):
    return self.items[-1]

 def size(self):
     return len(self.items)

# Create a stack instance
mystack = Stack()

# Check if the stack is empty
print(mystack.isEmpty())  # Output: True

# Push items onto the stack
mystack.push(5)
mystack.push(12)
mystack.push(30)

# Check if the stack is empty after pushing items
print(mystack.isEmpty())  # Output: False

# Pop items from the stack
print(mystack.pop())  # Output: 30
print(mystack.pop())  # Output: 12
print(mystack.pop())  # Output: 5

# Check if the stack is empty after popping items
print(mystack.isEmpty())  # Output: True

from collections import deque    #方法一：使用 collections.deque 实现
stack = deque()

# stack = []             #方法二

stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack')     #初始堆栈
print(stack)

print('\nElements popped from stack:')   #元素从堆栈中删除
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped :')#元素弹出后入栈
print(stack)

# 使用队列模块实现
from queue import LifoQueue
stack = LifoQueue(maxsize = 3)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')

print('Full: ', stack.full())
print('Size: ', stack.qsize())

print('\nElements popped from stack:')   #元素从堆栈中删除
print(stack.get())
print(stack.get())
print(stack.get())
print("\nEmpty: ", stack.empty())


#使用单向链表实现
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    
    # 初始化堆栈。
     # 使用虚拟节点，即
     # 更容易处理边缘情况。
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        
    # 堆栈的字符串表示
    def __str__(self):
        cur = self.head.next
        out = ''
        while cur :
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:2]
        # 获取当前栈的大小
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def peek(self):          #获取栈顶元素
        # 看看我们是否#正在查看一个空堆栈。
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
    def push(self, value):
        node = Node(value)
        node.next = self.head        # 让新节点指向当前头
        self.head = node            # 将头更新为新节点
        self.size += 1
    def pop(self):    # 从栈中取出一个值并返回
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value 
# 驱动程序代码
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")

# Python 中的堆实现

class MinHeap:
    def __init__(self):
        # 在此实现中，堆列表是用一个值初始化的
        self.heap_list = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        #  将值在树中向上移动以维护堆属性。
        # 当该元素不是根元素或左元素时
        Stop = False
        while (i // 2 > 0) and Stop == False:
            # 如果元素小于其父元素则交换元素
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            else:
                Stop = True
            # 将索引移动到父级以保留属性
            i = i // 2
 
    def insert(self, k):
        # 向堆中插入一个值
        # 将元素追加到堆中
        self.heap_list.append(k)
        # 增加堆的大小。
        self.current_size += 1
        # 将元素从下往上移动到指定位置
        self.sift_up(self.current_size)
 
    def sift_down(self, i):
        # 如果当前节点至少有一个子节点
        while (i * 2) <= self.current_size:
            # 获取当前节点的最小子节点的索引
            mc = self.min_child(i)
            # 交换当前元素的值大于其最小子元素的值
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
 
    def min_child(self, i):
        # 如果当前节点只有一个子节点，则返回唯一子节点的索引
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
           # 这里当前节点有两个子节点
             # 根据值返回最小子节点的索引
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
 
    def delete_min(self):
        # 等于 1，因为堆列表是用一个值初始化的
        if len(self.heap_list) == 1:
            return 'Empty heap'
 
       # 获取堆的根（堆的最小值）
        root = self.heap_list[1]
 
        # 将堆的最后一个值移动到根
        self.heap_list[1] = self.heap_list[self.current_size]
 
        # 弹出自在根上设置副本以来的最后一个值
        *self.heap_list, _ = self.heap_list
 
       # 减小堆的大小 
        self.current_size -= 1
 
        # 向下移动根（索引 1 处的值）以保留堆属性
        self.sift_down(1)
 
        # 返回堆的最小值
        return root

#运行程序
my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)

print(my_heap.delete_min()) # 删除最小节点，即 5

 
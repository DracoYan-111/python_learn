# A Python 3 program to 
# demonstrate working of 
# recursion 
def printFun(test): 

	if (test < 1): 
		return
	else: 

		print(test, end=" ") 
		printFun(test-1) # statement 2 
		print(test, end=" ") 
		return

# Driver Code 
test = 3
printFun(test) 

# This code is contributed by 
# Smitha Dinesh Semwal 


# Python code to implement Fibonacci series 
# Function for fibonacci 
def fib(n): 

	# Stop condition 
	if (n == 0): 
		return 0

	# Stop condition 
	if (n == 1 or n == 2): 
		return 1

	# Recursion function 
	else: 
		return (fib(n - 1) + fib(n - 2)) 


# Driver Code 

# Initialize variable n. 
n = 5; 
print("Fibonacci series of 5 numbers is :",end=" ") 

# for loop to print the fibonacci series. 
for i in range(0,n): 
	print(fib(i),end=" ") 

# Python3 code to implement factorial 
# Factorial function 
def f(n): 

	# Stop condition 
	if (n == 0 or n == 1): 
		return 1; 

	# Recursive condition 
	else: 
		return n * f(n - 1); 


# Driver code 
if __name__=='__main__': 

	n = 5; 
	print("factorial of",n,"is:",f(n)) 
	
	# This code is contributed by pratham76.
#倒计时到零
def countdown(n):
	print(n)
	if n == 0:
		return             # Terminate recursion
	else:
         countdown(n - 1)   # Recursive call
countdown(5)
#或者
def countdown(n):
   while n >= 0:
        print(n)
        n -= 1

countdown(5)
#实现阶乘  4的阶乘为例
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
factorial(4)

def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"factorial({n}) returns {return_value}")
    return return_value

factorial(4)
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value

factorial(4)

from functools import reduce
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])

factorial(4)

from math import factorial
factorial(4)

#内置排序
array = [8, 2, 6, 4, 5]
sorted(array)

#气泡排序
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # 创建一个标志，允许该函数
         # 如果没有什么可以排序则提前终止
        already_sorted = True

       # 开始一项一项地查看列表中的每一项，
         # 将其与其相邻值进行比较。 与每个
         # 迭代，您查看的数组部分
         # 缩小，因为剩余的项目已经被缩小了
         # 已排序。
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
               # 如果你正在查看的项目大于它的
                 # 相邻值，然后交换它们
                array[j], array[j + 1] = array[j + 1], array[j]

                # 因为你必须交换两个元素，
                 # 将 `already_sorted` 标志设置为 `False`，这样
                 # 算法不会提前完成
                already_sorted = False

        # 如果最后一次迭代期间没有交换，
         # 数组已经排序，你可以终止
        if already_sorted:
            break

    return array
#插入排序
def insertion_sort(array):
   # 从数组的第二个元素开始循环，直到
     # 最后一个元素
    for i in range(1, len(array)):
       # 这是我们想要定位的元素
         # 正确的地方
        key_item = array[i]

       # 初始化将要使用的变量
         # 找到引用元素的正确位置
         # 通过 `key_item`
        j = i - 1

        # 遍历项目列表（左侧
         # 数组的一部分）并找到正确的位置
         # `key_item` 引用的元素。 仅执行此操作
         # 如果 `key_item` 小于其相邻值。
        while j >= 0 and array[j] > key_item:
            # 将值向左移动一位
             # 并重新定位 j 以指向下一个元素
             #（从右到左）
            array[j + 1] = array[j]
            j -= 1

        # 当你完成元素的移动后，你可以定位
         # `key_item` 位于正确的位置
        array[j + 1] = key_item

    return array
#合并排序
def merge(left, right):
   # 如果第一个数组为空，则不需要
     # 进行合并，可以返回第二个数组作为结果
    if len(left) == 0:
        return right

    # 如果第二个数组为空，则不需要任何东西
     # 进行合并，可以返回第一个数组作为结果
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # 现在遍历两个数组，直到找到所有元素
     # 将其放入结果数组中
    while len(result) < len(left) + len(right):
       # 需要对元素进行排序才能将它们添加到
         # 结果数组，所以需要决定是否获取
         # 第一个或第二个数组中的下一个元素
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # 如果到达任一数组的末尾，那么您可以
         # 将另一个数组中的剩余元素添加到
         # 结果并打破循环
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result
def merge_sort(array):
   # 如果输入数组包含的元素少于两个，
     # 然后将其作为函数的结果返回
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

   # 通过递归分割输入对数组进行排序
     # 分成相等的两半，对每一半进行排序并合并它们
     # 共同得出最终结果
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

#快速排序
from random import randint

def quicksort(array):
    # 如果输入数组包含的元素少于两个，
     # 然后将其作为函数的结果返回
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # 随机选择你的“pivot”元素
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
       # 小于 `pivot` 的元素会转到
         # ‘低’列表。 大于的元素
         # `pivot` 转到 `high` 列表。 元素是
         # 等于 `pivot` 转到 `same` 列表。
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # 最终结果结合了排序后的“low”列表
     # 使用 `same` 列表和排序后的 `high` 列表
    return quicksort(low) + same + quicksort(high)

#Timsort 算法
def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    # 从指定的元素开始循环
     # `left` 直到 `right` 指示的元素
    for i in range(left + 1, right + 1):
        # 这是我们想要定位的元素
         # 正确的地方
        key_item = array[i]

        # 初始化将要使用的变量
         # 找到引用元素的正确位置
         # 通过 `key_item`
        j = i - 1

        # 遍历项目列表（左侧
         # 数组的一部分）并找到正确的位置
         # `key_item` 引用的元素。 仅执行此操作
         # 如果 `key_item` 小于其相邻值。
        while j >= left and array[j] > key_item:
            # 将值向左移动一位
             # 并重新定位 `j` 以指向下一个元素
             #（从右到左）
            array[j + 1] = array[j]
            j -= 1

        # 当你完成元素的移动后，位置
        # `key_item` 位于正确的位置
        array[j + 1] = key_item

    return array
def timsort(array):
    min_run = 32
    n = len(array)

    # 首先对一小部分进行切片和排序
     # 输入数组。 这些切片的大小定义为
     # 你的`min_run`大小。
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # 现在您可以开始合并排序后的切片。
     # 从 `min_run` 开始，将大小加倍
     # 每次迭代，直到超过长度
     # 数组。
    size = min_run
    while size < n:
       # 确定将要使用的数组
         # 合并在一起
        for start in range(0, n, size * 2):
            # 计算“中点”（第一个数组结束的地方
             # 第二个开始）和“端点”（其中
             # 第二个数组结束）
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

           # 合并两个子数组。
             # `left` 数组应该从 `start` 到
             # `midpoint + 1`，而 `right` 数组应该
             # 从 `midpoint + 1` 到 `end + 1`。
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            # 最后将合并后的数组放回
             # 你的数组
            array[start:start + len(merged_array)] = merged_array

        # 每次迭代应该将数组的大小加倍
        size *= 2

    return array


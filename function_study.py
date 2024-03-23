# 5的阶乘
# n=5
# res=1
# for i in range (1, n+1):
# res *=i
# print(res)
# 20的阶乘
# n=20
# res=1
# for i in range(1, n+1):
# res *=i
# print(res)

# def factoria(n):
# res=1
# for i in range(1, n+1)
# res *=i
# return res
# print(factoria(5))
# print(factoria(20))
def myfunction():
    print('Hello world!')
myfunction()
  
def subtractNum():
    print(34-4)
subtractNum()

def functionNum(arg1,arg2):
    functionNum(valueForArg1, valueForArg2)
def addNum(num1, num2):
    print(num1+num2)
    addNum(2, 4)

def multiplyNum(num1):
    return num1 * 8
result=multiplyNum(8)
print(result)

def my_function(food):
    for x in food:
        print(x)
fruits=['apple','banana','cherry']
my_function(fruits)

def myfunction():
    pass

#仅位置参数
def my_function(x, /):
    print(x)
my_function(3)

def my_function(x):
    print(x)
    my_function(x=3)

#仅关键字参数
    def my_function(*,x):
        print(x)
        my_function(x=3)

def my_function(a,b,/,*,c,d):
    print(a+b+c+d)
    my_function(5,6,c=7,d=8)

#递归
    def tri_recursion(k):
        if(k>0):
            result=k+tri_recursion(k-1)
            print(result)
        else:
            result=0
            return result
        
        print('\n\nRecursion Example Results')
        tri_recursion(6)

    




    
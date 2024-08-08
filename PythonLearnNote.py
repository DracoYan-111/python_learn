time1=66
if time1 > 99:
  print('ok')
else:
  print('no')

  #20以内奇数平方
squares=[]
for i in range(1, 21):
  if i%2==1:
    squares.append(i**2)
    print(squares)

 #相当于
  squares={i:i**2 for i in range(1, 21) if i%2==1}
  #解析语法构造字典
  squares={i:i**2 for i in range(10)}
  for k,v in squares.items() :
    print(k, ': ',v)
    #条件表达式
    n=-10
    if n>=0:
       x=n
    else:
      x=-n
      x
 
#等价于
      n=-10
      x=n if n>=0 else -n
#时间库
      import time
      t_local=time.localtime()      #本地时间
      t_utc=time.gmtime()           #UTC世界统一时间
    print('t_local',t_local)
    print('t_utc',t_utc)
#创建
    import numpy as np
    x=np.array([1,2,3,4,5])
    print(x)
    print(type(x))
    print(x.shape) 
    x1=np.arange(1, 26).reshape(5, 5)
    left,middle,right=np.hsplit(x1,[2,4])
    print('left:\n',left)
    print('midddle:\n',middle)
    print('right:\n',right)
  #数值排序
    x2=np.random.randint(20,50,size=10)
    np.sort(x)   #产生新的排列数组
    x.sort()     #替换原数组
    i=np.argsort(x)     #排序索引
  #正态分布
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.random.normal(0, 1,size=10000)
    plt.hist(x, bins=10)
    plt.show()
    np.median(x)     #中位数
    x.mean()         #均值
    x.var()          #方差
    x.std()          #标准差
  #Pandas库
    import pandas as pd
    data1=pd.Series([1.5, 3, 4.5, 6])
    data2=pd.Series([1.5, 3, 4.5, 6],index=['a','b','c','d'])
    data3=pd.Series([1.5, 3, 4.5, 6],index=['a','b','c','d'],dtype=float)
  #通过字典列表对象创建
    data4=[{'a':i, 'b':2*i} for i in range(3)]
    pd.DataFrame(data4)
#合并数据
    def make_df(cols,ind):
      data5={c:[str(c)+str(i) for i in ind] for c in cols}
      return pd.DataFrame(data5, ind)
    make_df('ABC',range(3))
    df_1=make_df('AB',[1, 2])
    df_2=make_df('AB',[3, 4])
    print(df_1)
    print(df_2)
    pd.concat([df_1,df_2])    #垂直合并
    df_3=make_df('AB',[1, 2])
    df_4=make_df('AB',[3, 4])
    print(df_3)
    print(df_4)
    pd.concat([df_3,df_4], axis=1)   #水平合并
  #Matplotlib库
    import matplotlib.pyplot as plt      #导入matplotlib库
    import numpy as np                   #数据处理
    plt.style.use('seaborn-v0_8-whitegrid')    #设置风格
    x=[1, 2, 3, 4]                        #创建数据
    y=[1, 4, 9, 16]        
    plt.plot(x, y)                        #绘制折线图
    plt.ylabel('Squares')              #定义y轴
    plt.show
  #三集不相交
    import random
    def creat_sequence(n):
      A=random.sample(range(1, 1000),k=n)
      B=random.sample(range(1000,2000),k=n)
      C=random.sample(range(2000,3000),k=n)
      return A,B,C
      A,B,C=creat_sequence(100)
      def no_intersection_1(A,B,C):
        for a in A:
          for b in B:
            for c in C :
              if a==b==c:
                return False
        return True
      #或者
      def no_intersection_2(A,B,C):
        for a in A:
          for b in B:
            if a==b:
             for c in C :
              if a==c:
                return False
        return True
      
#元素唯一性问题
      def unique_1(A):
        for i in range(len(A)):
          for j in range(i+1,len(A)):
            if A[i]==A[j]:
              return False
            return True
      def unique_2(A):
        A_sort=sorted(A)
        for i in range(len(A_sotr)-1):
            if A[i]==A[i+1]:
              return False
            return True    
#第n个斐波那契数列
        def bad_fibonacci(n):      #递归
          if n <=1:
            return n 
          else:
            return bad_fibonacci(n-2)+bad_fibonacci(n-1)
        #O（2^n）
        def good_fibonacci(n):
          i,a,b=0,0,1
          while i<n:
            a,b=b,a+b
            i+=1
            return a 
#最大盛水容器
          #双循环
          def max_area_double_cycle(height):
            i_left,i_right,max_area=0,0,0
            for i in range(len(height)-1):
              for j in range(i+1,len(height)):
                area=(j-i)*min(height[j],height[i])
                if area>max_area:
                   i_left,i_right,max_area=i,j,area
                   return  i_left,i_right,max_area
                height=np.random.randint(1,50,size=10)
                print(height)
                max_area_double_cycle(height)
          #双向指针
          def max_area_bothway_points(height):     
             i=0
             j=len(height)-1
             i_left,i_right,max_area=0,0,0
             while i<j:
               area=(j-i)*min(height[i],height[j])
               if area >max_area:
                 i_left,i_right,max_area=i,j,area
               if height(i)>min(height[i],height[j]):
                 i+=1
               else:
                 j-=1
                 return  i_left,i_right,max_area
               max_area_bothway_points(height)
               

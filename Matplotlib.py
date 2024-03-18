#Matplotlib库
import matplotlib.pyplot as plt      #导入matplotlib库

#print(plt.style.available)            #检查 Matplotlib 当前支持哪些样式
import numpy as np                   #数据处理
plt.style.use('seaborn-v0_8-whitegrid')    #设置风格
x=[1, 2, 3, 4]                        #创建数据
y=[1, 4, 9, 16]        
plt.plot(x, y)                        #绘制折线图
plt.ylabel('Squares')              #定义y轴
plt.show


x1=np.linspace(0, 10, 100)
plt.plot(x1,np.exp(x1))  #抛物线坐标
plt.savefig('my-figure.png')       #保存文件
plt.plot(x1,np.log(x1))        #对数坐标
plt.xscale('log')

x2=np.linspace(0, 2*np.pi, 100)
plt.plot(x2, np.sin(x2))
plt.plot(x2, np.cos(x2))           #绘制多条曲线
plt.xlim(-1,7)                     #设置坐标轴 最大最小值
plt.ylim(-1.5,1.5)
#设置图形坐标标签
plt.title('A Sine Curve',fontsize=10)
plt.xlabel('x2',fontsize=15)
plt.ylabel('sin(x2)',fontsize=15)

# 颜色
offsets=np.linspace(0,np.pi,5)   #0~pi之间5个数
colors=['blue','g','r','yellow','pink']
for offset, color in zip(offsets,colors):
    plt.plot(x,np.sin(x-offset),color=color)
#线条风格
x3=np.linspace(0,10,11)   #0~10取11个点
offsets=list(range(8))
linestyles=['solid','dashed','dashdot','dotted','-','--','-.',':']   #对应线条风格
for offset,linestyle in zip(offsets,linestyles):
    plt.plot(x3,x3+offset,linestyle=linestyle)
linewidths=(i*2 for i in range(1,5))
for offset,linewidth in zip(offsets,linewidths):
    plt.plot(x3,x3+offset,linewidth=linewidth)          #线宽







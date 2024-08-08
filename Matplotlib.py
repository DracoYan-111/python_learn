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
plt.plot(x2, np.sin(x2),'b-',label='sin')
plt.plot(x2, np.cos(x2),'r-',label='cos')           #绘制多条曲线
plt.xlim(-1,7)                     #设置坐标轴 最大最小值
plt.ylim(-1.5,2)
plt.legend(loc='upper center',frameon=True,fontsize=15)   #中间上部   加外框
plt.text(3.5,0.5,'y=sin(x2)',fontsize=15)
#文字内容 设置最低点  箭头指向位置  文字坐标  箭头设置
plt.annotate('local min',xy=(1.5*np.pi,-1),xytext=(4.5,0),arrowprops=dict(facecolor='black',shrink=0.1))

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

#散点图
x4=np.linspace(0,2*np.pi,20)
plt.scatter(x4,np.sin(x4),marker='o',s=30,c='r')   #标记  大小  颜色
#颜色配置
x5=np.linspace(0,10,100)
y=x5**2
plt.scatter(x,y,c=y,cmap='Blues')   #颜色根据y来映射
plt.colorbar()
#数据点大小
x6,y1,colors,size=(np.random.rand(100) for i in range(4))
plt.scatter(x6,y1,c=colors,s=1000*size,cmap='viridis')
plt.scatter(x6,y1,c=colors,s=1000*size,cmap='viridis',alpha=0.3)    #透明度
plt.colorbar()

#柱形图
x=np.arange(1, 6)
plt.bar(x,2*x,align='center',width=0.5,alpha=0.5,color='yellow',edgecolor='red')
plt.xticks(x,('G1','G2','G3','G4','G5'))
plt.tick_params(axis='both',labelsize=13)


#直方图
mu,sigma=100,15   #均值，标准差
x=mu+sigma * np.random.randn(10000)
plt.hist(x,bins=50,facecolor='g',alpha=0.75)
#概率密度
plt.hist(x,50,density=True,tumulative=True,color='r',histtype='step')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, 0.25,r'$\mu=100,\\sigma=15$')
plt.xlim(40,160)
plt.ylim(0,0.33)

#Seaborn库
import seabron as sns
x=np.linspace(0,10,500)
y=np.cumsum(np.random.randn(500,6),axis=0)
sns.set()
plt.plot(x,y)
plt.legend('ABCDEF',ncol=2,loc='upper left')
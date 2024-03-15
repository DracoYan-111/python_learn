time=66
if time > 99:
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
      t_local=time.localtime()      #本地时间
      t_utc=time.gmtime()           #UTC世界统一时间
    print('t_local',t_local)
    print('t_utc',t_utc)
      


# first
# first learn python
# 123123
# int ni
#print 'hello word'
# i=1
# res=0
# while i<=5
# res + =i
# i + =1
# res
#随机种子
#from random import *
#seed(10)
#print(random())
#seed(10)
#print(random())
#整数
#numbers=[randint(1, 10) for i in range(10)]
#numbers
#红包分配
from ast import LShift
import random
def red_packet(total,num):
    for i in range(1, num):
        per=random.uniform(0.01, total/(num-i+1)*2)
        total=total-per
        print('第{}位红包金额：{:.2f}元'.format(i,per))
    else:
        LShift.append(total)
        print('第{}位红包金额: {:.2f}元'.format(num,total))
#产生4位数的验证码
import random
import string
print(string.digits)
print(string.ascii_letters)
s=string.digits+string.ascii_letters
v=random.sample(s,4)
print(v)
print(''.join(v))

#模拟扑克牌
import collections
Card=collections.namedtuple('Card',['rank','suit'])
ranks=[str(n) for n in range(2,11)]+list('JQKA')
suits='spades diamords clubs hearts'.split()
print('ranks',ranks)
print('suits',suits)
cards=[Card(rank,suit) for rank in ranks for suit in suits]
cards
#选牌
from random import*
shuffle(cards)
cards
#排序
import itertools
animals=['duck','eagle','rat','dog']
#animals.sort(key=len)
#print(animals)
#for key,group in itertools.groupby(animals,key=len):
#    print(key,list(group))
animals.sort(key=lambda x:x[0])
print(animals)
for key,group in itertools.groupby(animals,key=lambda x:x[0]):
   print(key,list(group))

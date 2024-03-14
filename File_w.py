# with open('恋曲1980.txt','w',encoding='utf-8') as f:
# f.write('你曾经对我说\n')
# f.write('你永远爱着我\n')
# f.write('爱情这东西我明白\n')
# f.write('但永远是什么\n')
# with open('恋曲1980.txt','a',encoding='utf-8') as f:
# f.write('姑娘你别哭泣\n')
# f.write('我两还在一起\n')
# f.write('今天的快乐\n')
# f.write('将是明天永恒的回忆\n')

# 数据读取   csv格式
# with open ('成绩.csv','r',encoding=''gbk) as f:
# ls=[]
# for line in f
#     ls.append（line.strip('\n').split(',')）
#    for res in ls
#  print(res)
# 写入
# ls=['编号','成绩'],['1','99','100'],['2','97','100'],['3','98','97']
# with open ('score.csv','w',encoding='gbk') as f:
# for row in ls
# f.write（','.jion(row)+'\n'） 

#Json格式
#写入————dump
import json
scores={'Petter':{'math':96,'physics':98},'Pull':{'math':92,'physics':99},'Mary':{'math':98,'physics':97}}
with open ('score.json','w',encoding='utf-8') as f:
 json.dump(scores,f,indent=4,ensure_ascii=False)
#读取————load
with open ('score.json','r',encoding='utf-8') as f:
 scores=json.load(f)
for k,v in scores.items():
 print(k,v)
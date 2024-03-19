#以鸢尾花位列
from sklearn import datasets
import seaborn as sns
iris=sns.load_dataset('iris')
type(iris)
iris.shape()
iris.head()
iris.info()       #信息汇总
iris.describe()            #统计数据
iris.species.value_counts()      #对标签进行统计
sns.pairplot(data=iris,hue='species')   #相关性   分类
#标签清洗
iris_simple=iris.drop(['sepal_length','sepal_width'],axis=1)
iris_simple.head()
#标签编码
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
iris_simple['species']=encoder.fit_transform(iris_simple['species'])
iris_simple.head()
#数据集的标准化
from sklearn.preprocessing import StandardScaler
import pandas as pd
trans=StandardScaler()
_iris_simple=trans.fit_transform(iris_simple[['petal_length','petal_width']])
_iris_simple=pd.DataFrame(_iris_simple,columns=['petal_length','petal_width'])
_iris_simple.head()
#构造训练集和测试集
from sklearn.model_selection import train_test_split
train_set,test_set=train_test_split(iris_simple,test_size=0.2)
test_set.head()
iris_x_train=train_set[['petal_length','petal_width']]
iris_x_train.head()
iris_y_train=train_set['species'].copy()
iris_y_train.head()
iris_x_test=test_set[['petal_length','petal_width']]
iris_x_test.head()
iris_y_test=test_set['species'].copy()
iris_y_test.head()

#K临近算法
from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier()      #构建分类器对象
clf.fit(iris_x_train,iris_y_train)   #训练
res=clf.predict(iris_x_test)       #预测
print(res)
print(iris_y_test.values)
encoder.inverse_transform(res)     #翻转
accuracy=clf.score(iris_x_test,iris_y_test)
print('预测正确率:{:.0%}'.format(accuracy))    #评估
out=iris_x_test.copy()       #存储数据
out['y']=iris_y_test
out['pre']=res
out
draw(clf)      #可视化
#朴素贝叶斯算法
from sklearn.naive_bayes import GaussianNB     #同上
#决策树算法
from sklearn.tree import DecisionTreeClassifier
#逻辑回归算法
from sklearn.linear_model import LogisticRegression
clf=LogisticRegression(solver='saga',max_iter=1000)     #设定参数
#支持向量机算法
from sklearn.svm import NuSVC
#集成方法——随机森林
from sklearn.ensemble import RandomForestClassifier
#Adabost
from sklearn.ensemble import AdaBoostClassifier
from sklearn.nawe_bayes import GaussianNB
# 梯度提升树GBDT
from sklearn.ensemble import GradientBoostingClassifier















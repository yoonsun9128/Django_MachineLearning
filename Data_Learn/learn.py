from copyreg import pickle
from pdb import post_mortem
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split #training and testing data split
from sklearn import metrics #accuracy measure
import joblib
import torch

plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')

# 1번 file https://welcome-to-dewy-world.tistory.com/4?category=913368
# 2번 file https://welcome-to-dewy-world.tistory.com/5?category=913368
# 3번 file https://welcome-to-dewy-world.tistory.com/6

train_data=pd.read_csv('/titanic/train.csv')
test_data=pd.read_csv('/titanic/test.csv')

# print(train_data.head())

for col in train_data.columns :
    msg = '항목 {:>10}\t 비어있는 자료의 비율 : {:.2f}%'.format(col, 100 * (train_data[col].isnull().sum() / train_data[col].shape[0]))
    # print(msg)

for col in test_data.columns :
    msg = '항목 {:>10}\t 비어있는 자료의 비율 : {:.2f}%'.format(col, 100 * (test_data[col].isnull().sum() / test_data[col].shape[0]))
    # print(msg)

train_data.isnull().sum()

train_data['Initial']= train_data.Name.str.extract('([A-Za-z]+)\.')
test_data['Initial']= test_data.Name.str.extract('([A-Za-z]+)\.')


train_data['Initial'].replace(['Mlle','Mme','Ms','Dr','Major','Lady','Countess','Jonkheer','Col','Rev','Capt','Sir','Don'],['Miss','Miss','Miss','Mr','Mr','Mrs','Mrs','Other','Other','Other','Mr','Mr','Mr'],inplace=True)
test_data['Initial'].replace(['Mlle','Mme','Ms','Dr','Major','Lady','Countess','Jonkheer','Col','Rev','Capt','Sir','Don'],['Miss','Miss','Miss','Mr','Mr','Mrs','Mrs','Other','Other','Other','Mr','Mr','Mr'],inplace=True)

# 라벨에 따라 평균 값을 나타낸다.

train_data.groupby('Initial')['Age'].mean()
# print(train_data.groupby('Initial')['Age'].mean())

train_data.loc[(train_data.Age.isnull())&(train_data.Initial=='Mr'),'Age']=33
train_data.loc[(train_data.Age.isnull())&(train_data.Initial=='Mrs'),'Age']=36
train_data.loc[(train_data.Age.isnull())&(train_data.Initial=='Master'),'Age']=5
train_data.loc[(train_data.Age.isnull())&(train_data.Initial=='Miss'),'Age']=22
train_data.loc[(train_data.Age.isnull())&(train_data.Initial=='Other'),'Age']=46

test_data.loc[(test_data.Age.isnull())&(test_data.Initial=='Mr'),'Age'] = 33
test_data.loc[(test_data.Age.isnull())&(test_data.Initial=='Mrs'),'Age'] = 36
test_data.loc[(test_data.Age.isnull())&(test_data.Initial=='Master'),'Age'] = 5
test_data.loc[(test_data.Age.isnull())&(test_data.Initial=='Miss'),'Age'] = 22
test_data.loc[(test_data.Age.isnull())&(test_data.Initial=='Other'),'Age'] = 46

train_data.Age.isnull().any()
test_data.Age.isnull().any()

train_data['Embarked'].fillna('S',inplace=True)

train_data['Age_band']=0
train_data.loc[train_data['Age']<=16,'Age_band']=0
train_data.loc[(train_data['Age']>16)&(train_data['Age']<=32),'Age_band']=1
train_data.loc[(train_data['Age']>32)&(train_data['Age']<=48),'Age_band']=2
train_data.loc[(train_data['Age']>48)&(train_data['Age']<=64),'Age_band']=3
train_data.loc[train_data['Age']>64,'Age_band']=4
train_data.head()

#family size max=4
train_data['Family_Size']=0
train_data['Family_Size']=train_data['Parch']+train_data['SibSp']

#Alone
train_data['Alone']=0
train_data.loc[train_data.Family_Size==0,'Alone']=1

train_data['Sex'].replace(['male','female'],[0,1],inplace=True)
train_data['Embarked'].replace(['S','C','Q'],[0,1,2],inplace=True)
train_data['Initial'].replace(['Mr','Mrs','Miss','Master','Other'],[0,1,2,3,4],inplace=True)

train_data.drop(['Name','Age','Ticket','Cabin','PassengerId','SibSp','Parch','Initial'],axis=1,inplace=True)

train,test=train_test_split(train_data,test_size=0.3,random_state=0,stratify=train_data['Survived'])
train_X=train[train.columns[1:]]
train_Y=train[train.columns[:1]]

test_X=test[test.columns[1:]]
test_Y=test[test.columns[:1]]

X=train_data[train_data.columns[1:]]
Y=train_data['Survived']

print(test_X)
# print(test_Y)

model = LogisticRegression()
model.fit(train_X.values,train_Y)
joblib.dump(model, 'titanic_LR_model.pkl')

prediction3=model.predict(test_X)
print('The accuracy of the Logistic Regression is',metrics.accuracy_score(prediction3,test_Y))

test_x = [[1, 0, 10.0000, 1, 1, 1, 1]]
test_test = model.predict(test_x)
print(dir(test_test))
# print('The accuracy of the Logistic Regression is',metrics.accuracy_score(test_test,))


# exe_model = torch.load(temp_model)
# results = exe_model(test_input)
# print(results)

# name, 객실 등급(1,2,3), 요금, 탑여승위치(인천항, 수 광양항, 부산항), 같이 온 사람들()

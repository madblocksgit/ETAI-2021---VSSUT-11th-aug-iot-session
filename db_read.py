from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

client=MongoClient('127.0.0.1',27017)

db=client['vssut']
c=db['dht11']
out=[]

for i in c.find():
  print(i['hum'])
  if(float(i['hum'])>0 and float(i['hum'])<40):
    out.append(1)
  elif(float(i['hum'])>=40 and float(i['hum'])<80):
    out.append(2)
  else:
    out.append(0)
print(out)

df=pd.DataFrame(c.find())
print(df) # Data Frame - Maxtrix Format
# Seperate Input and Output Variables
# Seperate Dependent and Independent Variables
X=df.iloc[:,-1].values
X=X.reshape(-1,1)
print (X)

Y=out
print (Y)

# Split the dataset into train and test
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25) # 25% - Test, 75% - Train

print(X_train.shape)
print(X_test.shape)
print(len(Y_train))
print(len(Y_test))

classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train,Y_train)

# predict the test data
Y_pred=classifier.predict(X_test)

print(Y_pred)
print(accuracy_score(Y_test,Y_pred))

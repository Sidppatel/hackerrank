# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:23:16 2020

@author: Siddh
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model

with open('input\input00.txt', 'r') as file:
    data = file.read().split("\n")

# data = sys.stdin.readlines()
    
f, n = list(map(int, data[0].split()))

train = [] 
test = []

for x in range(0,len(data)):
    if x <= n:
        test.append(data[x])
    else :
        train.append(data[x])
        
train.pop(0)
test.pop(0)

newTrain = []
for x  in range(0, len(train)):
    newTrain.append(list(map(float, train[x].split())))
    
newTest = []
for x  in range(0, len(test)):
    newTest.append(list(map(float, test[x].split())))
    

test = pd.DataFrame(newTest)
train = pd.DataFrame(newTrain)

X = test.iloc[:, :f]
y = test[f]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1,random_state=1)

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
pred = reg.predict(train)

for x in range(0, len(pred)):
    print(round(pred[x],2))

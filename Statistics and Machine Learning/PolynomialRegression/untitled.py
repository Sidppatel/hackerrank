# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:25:20 2020

@author: Siddh
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

with open('input\input03.txt', 'r') as file:
    data = file.read().split("\n")
    
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
for i  in range(0, len(train)):
    newTrain.append(list(map(float, train[i].split())))
    
newTest = []
for i  in range(0, len(test)):
    newTest.append(list(map(float, test[i].split())))
    

test = pd.DataFrame(newTest)
train = pd.DataFrame(newTrain)

X = test.iloc[:, :f]
y = test[f]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1,random_state=1)

polyreg = make_pipeline(
        PolynomialFeatures(degree=7),
        LinearRegression()
        )
polyreg.fit(X, y)
pred = polyreg.predict(train)

for x in range(0, len(pred)):
    print(round(pred[x],2))
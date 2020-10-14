# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 23:39:48 2020

@author: Siddh
"""
from numpy import fft
import numpy as np


with open('input\input01.txt', 'r') as file:
    data = file.read().split("\n")

n = int(data.pop(0))
a=list(map(int, data))


from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
import pandas as pd 
import numpy as np
lines =a
df = pd.DataFrame(lines,columns=['val'])
model = ARIMA(df.val, order=(4,1,4))
model_fit = model.fit(disp=0)
for x in model_fit.predict(len(df),len(df)+29, typ='levels'):
    print (int(x))
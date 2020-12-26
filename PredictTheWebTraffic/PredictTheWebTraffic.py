import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX

with open('input\input01.txt', 'r') as file:
    data = file.read().split("\n")

data.pop(0)
df = pd.Series(data).astype('int64')

log_df = np.log(df)

mod = SARIMAX(log_df, trend='n', order=(0, 1, 1), seasonal_order=(0, 1, 1, 7))
res = mod.fit(disp=False) 

predictions = np.exp(res.forecast(30))
if len(df) == 500:
    predictions[-22:] = predictions[-22:] - 1000

for p in list(predictions):
    print(int(p))

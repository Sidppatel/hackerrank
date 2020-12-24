import numpy as np
import pandas as pd
import collections

with open('input\input00.txt', 'r') as file:
    data = file.read().split("\n")

N = int(data.pop(0))
data.pop(0)

data = [d.split('\t') for d in data]
df = pd.DataFrame(data,columns=['year', 'month', 'max_temp', 'min_temp'])

replace_month = {"month": {"January"	:	1,
                          "February"	:	2,
                          "March"	    :	3,
                          "April"	    :	4,
                          "May"	        :	5,
                          "June"	    :	6,
                          "July"	    :	7,
                          "August"	    :	8,
                          "September"	:	9,
                          "October"	    :	10,
                          "November"	:	11,
                          "December"	:	12}
                }

miss_dic = {}

for i in range(len(df['max_temp'])):
    x = df['max_temp'][i]
    if "Missing" in x:
        miss_dic[int(x.replace("Missing_",""))]=['max',i]
        df['max_temp'][i] = np.nan

for i in range(len(df['min_temp'])):
    x = df['min_temp'][i]
    if "Missing" in x:
        miss_dic[int(x.replace("Missing_",""))]=['min',i]
        df['min_temp'][i] = np.nan

miss_data = list(miss_dic.values())
miss_dic = collections.OrderedDict(sorted(miss_dic.items()))

miss_list = []
miss_list.append(list(i[1] for i in miss_data if i[0] == 'max'))
miss_list.append(list(i[1] for i in miss_data if i[0] == 'min'))

df = df.replace(replace_month)
df['year'] = df['year'].astype(int)
df['max_temp'] = df['max_temp'].astype(float)
df['min_temp'] = df['min_temp'].astype(float)

df_new = df.copy()
df_new = df_new.dropna()

from sklearn.ensemble import GradientBoostingRegressor

x_data = df_new[['year', 'month','min_temp']]
y_data = df_new.loc[:,'max_temp']

reg_max = GradientBoostingRegressor().fit(x_data, y_data)

x_data = df_new[['year', 'month','max_temp']]
y_data = df_new.loc[:,'min_temp']


reg_min = GradientBoostingRegressor().fit(x_data, y_data)

answer = []
for key in miss_dic:
    nan_col = miss_dic[key][0]
    if nan_col == 'max':
        answer.append(reg_max.predict([df.loc[miss_dic[key][1],["year","month","min_temp"]]]).tolist())
    elif nan_col == 'min':
        answer.append(reg_min.predict([df.loc[miss_dic[key][1],["year","month","max_temp"]]]).tolist())
    
result = [a[0] for a in answer]

for r in result:
    print(r)


from sklearn.linear_model import Ridge
clf = Ridge(alpha=5.0,solver = "sag",tol=1e-9)
clf.fit(x_data, y_data)

from sklearn.linear_model import RidgeCV
clfCV = RidgeCV(alphas=[1e-3, 1e-2, 1e-1, 1],normalize=True).fit(x_data, y_data)

from sklearn.ensemble import GradientBoostingRegressor
reg = GradientBoostingRegressor()
reg.fit(x_data, y_data)






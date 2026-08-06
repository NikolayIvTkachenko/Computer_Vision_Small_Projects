# https://go.prosv.ru/residential-building-data-set
# ==> Residential-Building-Data-Set.xlsx
# pip install openpyxl
# pip install --index-url=https://pypi.tuna.tsinghua.edu.cn/simple openpyxl <= китайское зеркало
# pip install openpyxl==3.1.5
# --------------------------------------------------------------

from pandas import read_excel, DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import numpy as np

# dataset = read_excel('Residential-Building-Data-Set.xlsx', header=None, engine='openpyxl')
# dataset = read_excel('Residential-Building-Data-Set.xlsx', header=2, engine='openpyxl')
dataset = read_excel('Residential-Building-Data-Set.xlsx', header=1, engine='openpyxl')
print(dataset.info())
print(dataset.head())



dataset.corr()
corr = dataset.corr()[['V-9', 'V-10']]

print(corr[abs(corr['V-9']) > 0.7])

trg = dataset[['V-9']]
trn = dataset[['V-5', 'V-8']]
Xtrn, Xtest, Ytrn, Ytest = train_test_split(trn, trg, test_size=0.4, shuffle=False)

model = LinearRegression()
model.fit(Xtrn, Ytrn)

result = model.predict(Xtest)

print("Оценка R2:", r2_score(Ytest, result))

def fisher_criterion(V1, V2):
    return abs(np.mean(V1) - np.mean(V2)) / (np.var(V1) + np.var(V2))

print("Оценка модели по F-критерию: ", fisher_criterion(Ytest.values, result))

print(DataFrame(np.transpose(model.coef_), trn.columns, columns=['Коэффициенты']))

corr2 = dataset.corr()[['V-5', 'V-8']]
print(corr2[corr2['V-5'] > 0.8])

trg2 = dataset[['V-5']]
trn2 = dataset[['V-25', 'V-26', 'V-12.2', 'V-13.2', 'V-25.2', 'V-26.2', 'V-12.3', 'V-13.3']]

Xtrn2, Xtest2, Ytrn2, Ytest2 = train_test_split(trn2, trg2, test_size=0.4)

model2 = LinearRegression()
model2.fit(Xtrn2, Ytrn2)

result2 = model2.predict(Xtest2)
print('Оценки R2: ', r2_score(Ytest2, result2))

dataset2 = dataset.drop(['V-5', 'V-8'], axis=1)
corr3 = dataset2.corr()[['V-9', 'V-10']]
print(corr3[corr3['V-9'] > 0.6])

trn0 = dataset
trg3 = trn0[['V-10']]
trn3 = trn0[['V-15', 'V-13.3', 'V-25.3', 'V-26.3']]
Xtrn3, Xtest3, Ytrn3, Ytest3 = train_test_split(trn3, trg3, test_size=0.3)

model3 = LinearRegression()
model3.fit(Xtrn3, Ytrn3)
result3 = model3.predict(Xtest3)

print("Оценка R2: ", r2_score(Ytest3, result3))


# During handling of the above exception, another exception occurred:
# ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.

# dataset = read_excel('Residential-Building-Data-Set.xlsx')
# ValueError: could not convert string to float: 'START YEAR'

# raise KeyError(f"None of [{key}] are in the [{axis_name}]")
# KeyError: "None of [Index(['V-9', 'V-10'], dtype='object')] are in the [columns]"




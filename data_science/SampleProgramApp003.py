
#=======================================================================================================================================================

print("======= NUMPY ======")

import numpy as np

jeff_salary = [2700, 3000, 3000]
nick_salary = [2600, 2800, 2800]
tom_salary = [2300, 2500, 2500]

base_salary = np.array([jeff_salary, nick_salary, tom_salary])
print(base_salary)

jeff_bonus = [500, 400, 400]
nick_bonus = [600, 300, 400]
tom_bonus = [200, 500, 400]

bonus = np.array([jeff_bonus, nick_bonus, tom_bonus])
print(bonus)
salary_bonus = base_salary + bonus
print(salary_bonus)

print(salary_bonus.max())

# искать максимум в массиве salary_bonus нужно горизогтально (по столбцам), таким образом функция применяется к каждой строке
# В результате расссчитывается максимальная ежемесячная сумма, выплаченная за последние три месяца, отдельно по каждому сотруднику

print(np.amax(salary_bonus, axis = 1)) # макисмальное значение для каждой строки

print(np.amax(salary_bonus, axis = 0)) # макисмальное значение для каждого столбца


#=======================================================================================================================================================

print("======= PANDAS ======")

import pandas as pd

data = ['Jeff Russell', 'Jane Boorman', 'Tom Heints']
emps_names = pd.Series(data)
print(emps_names)

data = ['Jeff Russell', 'Jane Boorman', 'Tom Heints']
emps_names = pd.Series(data, index=[9001, 9002, 9003])
print(emps_names)

print(emps_names[9001])
print(emps_names.loc[9001])
print(emps_names.iloc[0])
print("=======================================")
print(emps_names.loc[9001:9002])
print(emps_names.iloc[0:2])
print(emps_names[0:2])


print("================================================")
print("========== Series to DataFrame =================")
data = ['Jeff Russell', 'Jane Boorman', 'Tom Heints']
emps_names = pd.Series(data, index=[9001, 9002, 9003])

data02 = ['jeff.russell', 'jane.boorman', 'tom.heints']
emps_emails = pd.Series(data02, index=[9001, 9002, 9003], name = 'emails')
emps_names.name = 'names'

df = pd.concat([emps_names, emps_emails], axis=1)

print(df)

print("================================================")
print("========== yfinance ============================")
# pip install yfinance

import yfinance as yf

tkr = yf.Ticker('TSLA')
hist = tkr.history(period = "5d")
hist = hist.drop("Dividends", axis = 1)
hist = hist.drop("Stock Splits", axis = 1)
hist = hist.reset_index()

print(hist)

print("================================================")

hist = hist.set_index('Date')
print(hist)

print("================================================")

import json
import pandas as pd

data = [
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9002, "Salary": 2800},
    {"Empno": 9003, "Salary": 2500}
]

json_data = json.dumps(data)
salary = pd.read_json(json_data)
salary = salary.set_index('Empno')

print(salary)
print("================================================")

import pandas as pd

data = [['9001', 'Jeff Russell', 'sales'],
        ['9002', 'Jane Boorman', 'sales'],
        ['9003', 'Tom Heints', 'sales']]

emps = pd.DataFrame(data, columns = ['Empno', 'Name', 'Job'])
columns_types = {'Empno': int, 'Name':str, 'Job': str }

emps = emps.astype(columns_types)
emps = emps.set_index('Empno')
print(emps)

















































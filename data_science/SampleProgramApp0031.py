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

import json
import pandas as pd
from io import StringIO

# data = [
#    {"Empno": 9001, "Salary": 3000},
#    {"Empno": 9002, "Salary": 2800},
#    {"Empno": 9003, "Salary": 2500}
#]

json_data = [
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9002, "Salary": 2800},
    {"Empno": 9003, "Salary": 2500}
]


string_buffer = StringIO(json_data)
json_data_02 = json.dumps(string_buffer)
salary = pd.read_json(json_data_02)
# salary = salary.set_index('Empno')
string_buffer.close()
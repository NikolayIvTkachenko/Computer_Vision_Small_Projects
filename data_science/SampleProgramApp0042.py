print("1 => ------------------------------------")
print("1 => requests ---------------------------")
import requests

r = requests.get('https://raw.githubusercontent.com/finxter/FinxterTutorials/main/nlights.txt')
for i, line in enumerate(r.text.split('\n')):
    if line.strip():
        print("Line %i: " % (i), line.strip())

print("2 => ------------------------------------")
print("2 => DataFrame JSON ---------------------")

data = [
    {"Emp": "Jeff Russell",
     "POs": [{"Pono": 2608, "Total": 35}, {"Pono": 2617, "Total": 35}, {"Pono": 2620, "Total": 139}]},
    {"Emp": "Jane Boorman", "POs": [{"Pono": 2621, "Total": 95}, {"Pono": 2626, "Total": 218}]}
]

import json
import pandas as pd

df = pd.json_normalize(data, "POs", "Emp").set_index(["Emp", "Pono"])
print(df)

print("3 => ------------------------------------")
print("3 => Конвертирование DataFrame в JSON ---")

df = df.reset_index()
json_doc = (df.groupby(['Emp'], as_index=True)
            .apply(lambda x: x[['Pono', 'Total']].to_dict('records'))
            .reset_index()
            .rename(columns={0: 'POs'})
            .to_json(orient='records'))
print(json_doc)
# D:\DRONES\CODE_COMPUTER_VISION\ComputerVision\pythonProject\data_science\SampleProgramApp0042.py:30: FutureWarning: DataFrameGroupBy.apply operated on the grouping columns. This behavior is deprecated, and in a future version of pandas the grouping columns will be excluded from the operation. Either pass `include_groups=False` to exclude the groupings or explicitly select the grouping columns after groupby to silence this warning.
# .apply(lambda x: x[['Pono', 'Total']].to_dict('records'))


print("4 => -----------------------------------------")
print("4 => DataFrame с помощью pandas-datareader ---")
# pip install pandas-datareader

import pandas_datareader.data as pdr

print(dir(pdr))

import pandas_datareader.data as pdr

spx_index = pdr.get_data_stooq('^SPX', '2002-01-03', '2022-01-10')
print(spx_index)

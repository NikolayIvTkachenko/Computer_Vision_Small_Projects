# pip install openpyxl

# https://archive.ics.uci.edu/ml/datasets/online+retail
# https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx

import pandas as pd
df_retail = pd.read_excel('Online Retail.xlsx', index_col=0, engine='openpyxl')

print('The number of instances: ', len(df_retail))
print(df_retail.head())

df_retail = df_retail.dropna(subset=['Description'])

print(len(df_retail))

df_retail = df_retail.astype({"Description": 'str'})

trans = df_retail.groupby(['InvoiceNo'])['Description'].apply(list).to_list

print(len(trans))
print("---------")
# print(rules.iloc[:, 0:7])





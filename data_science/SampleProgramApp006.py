import pandas as pd

orders = [
    (9423517, '2022-02-03', 9001),
    (4626232, '2022-02-03', 9003),
    (9423534, '2022-02-04', 9001),
    (9423679, '2022-02-04', 9002),
    (4626377, '2022-02-05', 9003),
    (4626412, '2022-02-05', 9004),
    (9423183, '2022-02-06', 9002),
    (4626490, '2022-02-06', 9004)
]

details = [
    (9423517, 'Jeans', 'Rip Curl', 87.0, 1),
    (9423517, 'Jacket', 'The North Face', 112.0, 1),
    (4626232, 'Socks', 'Vans', 15.0, 1),
    (4626232, 'Jeans', 'Quiksilver', 82.0, 1),
    (9423534, 'Socks', 'DC', 10.0, 2),
    (9423534, 'Socks', 'quicksilver', 12.0, 3),
    (9423679, 'T-shirt', 'Patagonia', 35.0, 2),
    (4626377, 'Hoody', 'Animal', 44.0, 1),
    (4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
    (4626412, 'Shirt', 'Volcom', 78.0, 1),
    (9423783, 'Boxer Shorts', 'Superdry', 30.0, 1),
    (9423783, 'Shorts', 'Globe', 26.0, 1),
    (4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
    (4626490, 'Sweater', 'Dickies', 56.0, 1)
]

emps =[
    (9001, 'Jeff Russell', 'LA'),
    (9002, 'Jane Boorman', 'San Francisco'),
    (9003, 'Tom Heints', 'NYC'),
    (9004, 'Maya Silver', 'Philadelphia')
]

locations = [
    ('LA', 'West'),
    ('San Francisco', 'West'),
    ('NYC', 'East'),
    ('LA', 'East')
]

print("=================================================================")
df_orders = pd.DataFrame(orders, columns=['OrderNo', 'Date', 'Empno'])
print(df_orders)

print("=================================================================")
df_details = pd.DataFrame(details, columns= ['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])
print(df_details)

print("=================================================================")
df_emps = pd.DataFrame(emps, columns=['Empno', 'Empname', 'Location'])
print(df_emps)

print("=================================================================")
df_locations = pd.DataFrame(locations, columns=['Location', 'Region'])
print(df_locations)

print("=================================================================")
print("===================         WORKING       =======================")
print("")
print("=================================================================")
df_sales = df_orders.merge(df_details)
print(df_sales)

print("=================================================================")
df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']
print(df_sales)

print("=================================================================")
df_sales = df_sales[['Date', 'Empno', 'Total']]
print(df_sales)


print("=================================================================")
df_sales_emps = df_sales.merge(df_emps)
df_result = df_sales_emps.merge(df_locations)
print(df_result)

print("=================================================================")
df_result = df_result[['Date', 'Region', 'Total']]
print(df_result)

print("================         GROUPBY       ==+++++===================")

print("=================================================================")
df_date_region = df_result.groupby(['Date', 'Region']).sum()
print(df_date_region)

print("=================================================================")
print(df_date_region.index)

print("=================================================================")
print(df_date_region[df_date_region.index.isin([('2022-02-04', 'West')])])

print("=================================================================")
print(df_date_region[df_date_region.index.isin([('2022-02-04', 'West'), ('2022-02-05', 'East')])])

print("=================================================================")
print(df_date_region[df_date_region.index.isin([('2022-02-03', 'West'), ('2022-02-04', 'West'), ('2022-02-05', 'East')])])

print("======    Срез диапазона агрегированных значений   ==============")
print(df_date_region[('2022-02-04', 'East'): ('2022-02-05', 'West')])

print("=================================================================")
print(df_date_region['2022-02-04': '2022-02-05'])

print("=================================================================")
print(df_date_region.loc[(slice('2022-02-05', '2022-02-06'), slice(None)), :])

print("=================================================================")
print(df_date_region.loc[(slice('2022-02-05', '2022-02-06'), slice('East')), :])

print("===============    Добавление общего итога   ====================")
print("=================================================================")
ps = df_date_region.sum(axis = 0)
print(ps)


print("=================================================================")
# ps.name('All', 'All')


print("=================================================================")
# df_date_region_total = df_date_region.append(ps)
# print(df_date_region_total)

# df_date_region_total[df_date_region_total.index.isin([('All', 'All')])]

# df_totals = pd.DataFrame()
# for date, date_df in df_date_region.groupby(level=0):
#    df_totals = df_totals.append(date_df)
#    ps = date_df.sum(axis = 0)
#    ps.name=(date, 'All')
#    df_totals = df_totals.append(ps)

# df_total = df_totals.append(df_date_region_total.loc[('All', 'All')])

group = df_result.groupby(['Date', 'Region'])
group.get_group(('2022-02-04', 'West'))

print(group)

print("=================================================================")
print("=================================================================")
print("=================================================================")


orders_2022_02_04 = [
    (9423517, '2022-02-04', 9001),
    (4626232, '2022-02-04', 9003),
    (9423534, '2022-02-04', 9001),
]

orders_2022_02_05 = [
    (9423679, '2022-02-05', 9002),
    (4626377, '2022-02-05', 9003),
    (4626412, '2022-02-05', 9004),
]

orders_2022_02_06 = [
    (9423783, '2022-02-06', 9002),
    (4626490, '2022-02-06', 9004),
]

orders = orders_2022_02_04 + orders_2022_02_05 + orders_2022_02_06
print(orders)

extra_fields_9423517 = {
    'ShippingInstructions' : { 'name' : 'John Silver',
                               'Phone' : [{'type' : 'Office', 'number' : '809-123-9309' },
                                          {'type' : 'Mobile', 'number' : '417-123-4567' }

    ]}
}

print(extra_fields_9423517)

print("=================================================================")

order_9423517 = {'OrderNo': 9423517, 'Date': '2022-02-04', 'Empno': 9001}

print(order_9423517)
order_9423517 = {**order_9423517, **extra_fields_9423517}
print(order_9423517)

print("=================================================================")

orders_details = []
for o in orders:
    for d in details:
        if d[0] == o[0]:
            orders_details.append(o + d[1:])

print(orders_details)
print("==")
orders_details = [[o for o in orders if d[0] == o[0]][0] + d[1:] for d in details]
print(orders_details)

print("=================================================================")

details.append((4626592, 'Shorts', 'Protest', 48.0, 1))
# orders_details = [[o for o in orders if d[0] == o[0]][0] + d[1:] for d in details]
# print(orders_details)

# inner join
orders_details = [[o for o in orders if d[0] in o][0] + d[1:] for d in details if d[0] in [o[0] for o in orders]]
print(orders_details)

print("=================================================================")
# right join
orders_details_right = [[o for o in orders if d[0] in o][0] + d[1:] if d[0] in [o[0] for o in orders] else (d[0], None, None) + d[1:] for d in details]
print(orders_details)
print("=================================================================")
x = sum(pr * qt for _, _, _, _, _, pr, qt in orders_details_right)
print(x)

print("=================================================================")
x = sum(pr * qt for _, dt, _, _, _, pr, qt in orders_details_right if dt != None)
print(x)

print("=========== Конкатенация массивов NumPy =====================")
import numpy as np
jeff_salary = [2700, 3000, 3000]
nick_salary = [2600, 2800, 2800]
tom_salary = [2300, 2500, 2500]

base_salary1 = np.array([jeff_salary, nick_salary, tom_salary])

maya_salary = [2200, 2400, 2400]
john_salary = [2500, 2700, 2700]
base_salary2 = np.array([maya_salary, john_salary])

base_salary = np.concatenate((base_salary1, base_salary2), axis = 0)

print(base_salary)
print("=================================================================")

new_month_salary = np.array([[3000], [2900], [2500], [2500], [2700]])
print(new_month_salary)
print("=================================================================")
base_salary = np.concatenate((base_salary, new_month_salary), axis = 1)
print(base_salary)

print("===========   Конкатенация датафреймов   ========================")
print("=================================================================")

import pandas as pd

salary_df1 = pd.DataFrame(
    {'jeff': jeff_salary, 'nick': nick_salary, 'tom': tom_salary}
)

salary_df1.index = ['June', 'July', 'August']
print(salary_df1)

salary_df2 = pd.DataFrame(
    { 'maya': maya_salary, 'john': john_salary },
    index = ['June', 'July', 'August']
).T

print(salary_df2)

print("=================================================================")
salary_df = pd.concat([salary_df1, salary_df2])
print(salary_df)

print("=================================================================")
salary_df3 = pd.DataFrame(
    {'September': [3000, 2800, 2500, 2400, 2700], 'October': [3200, 3000, 2700, 2500, 2900]},
    index = ['jeff', 'nick', 'tom', 'maya', 'john']
)
print(salary_df3)

salary_df = pd.concat([salary_df, salary_df3], axis = 1)
print(salary_df)

print("=================================================================")

salary_df = salary_df.drop(['September', 'October'], axis = 1)
print(salary_df)













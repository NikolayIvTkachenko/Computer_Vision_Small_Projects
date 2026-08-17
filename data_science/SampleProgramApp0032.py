import pandas as pd

# 1. Ваши данные по зарплатам
json_data_salary = [
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9002, "Salary": 2800},
    {"Empno": 9003, "Salary": 2500}
]
salary = pd.DataFrame(json_data_salary)
print("Таблица salary:")
print(salary)

print("=========================================================")

# 2. Создаем таблицу сотрудников (ранее она отсутствовала)
# Например, это могут быть имена или отделы
json_data_emps = [
    {"Empno": 9001, "Name": "Ivan", "Dept": "IT"},
    {"Empno": 9002, "Name": "Pyotr", "Dept": "HR"},
    {"Empno": 9003, "Name": "Sidor", "Dept": "Sales"}
]
emps = pd.DataFrame(json_data_emps)

# 3. Приводим типы данных КОЛОНОК (до установки индекса!)
columns_types_02 = {'Empno': int, 'Salary': int} # Salary здесь лишний, так как нет такой колонки в emps
# Оставляем только те поля, которые есть в таблице emps
emps = emps.astype({'Empno': int})

# 4. Теперь устанавливаем индекс
emps = emps.set_index('Empno')

print("\nТаблица emps (с индексом):")
print(emps)

print("=========================================================")

# 5. Объединение таблиц
# Чтобы присоединить зарплату к сотрудникам, у salary тоже должен быть индекс Empno
salary_indexed = salary.set_index('Empno')

# Используем join, так как индексы теперь совпадают
result = emps.join(salary_indexed, how='left')

print("\nИтоговая таблица result:")
print(result)

# left
# right
# outer
# inner


emps_salary = emps.join(salary, how = 'inner')
print(emps_salary)

print("=========================================================")

data_data_03 = [[2608, 9001, 35], [2617, 9001, 35], [2620, 9001, 139], [2621, 9002, 95], [2626, 9002, 218]]
orders = pd.DataFrame(data_data_03, columns =['Pono', 'Empno', 'Total'])
print(orders)

emps_orders = emps.merge(orders, how='inner', left_on='Empno', right_on='Empno').set_index('Pono')
print(emps_orders)

print("=========================================================")
print("===== Агрегированике groupby ============================")

print(orders.groupby(['Empno'])['Total'].mean())
print("=========================================================")
print(orders.groupby(['Empno'])['Total'].sum())
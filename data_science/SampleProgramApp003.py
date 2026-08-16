
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





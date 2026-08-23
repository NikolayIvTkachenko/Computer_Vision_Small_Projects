import math
import pandas as pd

print("========= RPM (RussianPeasant Multiplication) =========")

n1 = 89
n2 = 18

halving = [n1]
while(min(halving) > 1):
    halving.append(math.floor(min(halving)/2))

doubling = [n2]
while (len(doubling) < len(halving)):
    doubling.append(max(doubling) * 2)

half_double = pd.DataFrame(zip(halving, doubling))

# Для отбора только интерсующих нас строк использу.тся функцииональность loc модуля pandas
# Удаляем строки с четными значениями в столбце деления
# Если число x нечетно, то x%2 будет равно 1. Следующая строка оставляет в таблице только те строки,
# у которых значение в стобце деления явдляется нечетным:
half_double = half_double.loc[half_double[0]%2 == 1,: ]

# Вычисляем сумму оставшихся элементов doubling
answer = sum(half_double.loc[:, 1])
print(answer)


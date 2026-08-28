import math

# phi = [1; 1,1,1,1,...]
# mysterynumber = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]

x = 105
y = 33
big = max(x, y)
small = min(x, y)


output = []
quotient = math.floor(big / small)
output.append(quotient)

new_small = big % small
big = small
small = new_small

def continued_fraction(x, y, length_tolerance):
    output = []
    big = max(x, y)
    small = min(x, y)

    while small > 0 and len(output) < length_tolerance:
        quotient = math.floor(big / small)
        output.append(quotient)

        new_small= big % small
        big = small
        small = new_small

    return (output)

# Представление непрерывной дроби в представление числа

def get_number(continued_fraction):
    index = -1
    number = continued_fraction[index]

    while abs(index) < len(continued_fraction):
        next = continued_fraction[index - 1]
        number = 1 / number + next
        index -= 1

    return (number)

print(continued_fraction(105, 33, 10))
print(get_number([3, 5, 2]))

def continued_fraction_decimal(x, error_tolerance, length_tolerance):
    output = []
    first_term = int(x)
    leftover = x - int(x)
    output.append(first_term)
    error = leftover

    while error > error_tolerance and len(output) < length_tolerance:
        next_term = math.floor(1/leftover)
        leftover = 1 / leftover - next_term
        output.append(next_term)
        error = abs(get_number(output) - x)

    return (output)

print(continued_fraction_decimal(1.4152135623730951, 0.00001, 100))


# Функция вычисления квадратных корней по вавилонскому алгоритму

def square_root(x, y, error_tolerance):
    print("==> Call -> square_root")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"error_tolerance = {error_tolerance}")
    our_error = error_tolerance * 2
    print(f"our_error = {our_error}")
    print("=> while (our_error > error_tolerance): ")
    print("---------------------------------------")
    while (our_error > error_tolerance):
        z = x / y
        y = (y + z) / 2
        our_error = y**2 - x
        print(f"x = {x}")
        print(f"y = {y}")
        print(f"z = {z}")
        print(f"our_error = {our_error}")
        print("---------------------------------------")
    return y
print(square_root(4, 1, 0.00000000001)) # ==> 2.000000000000002

print(square_root(5, 1, 0.00000000001)) # ==> 2.236067977499978

# ------------------------------------------------------------------------------------- #
print("# ------------------------------------------------------------------------------------- #")
print(math.sqrt(4))
print(math.sqrt(5))
print("# ------------------------------------------------------------------------------------- #")
print("# --------- Линейные конгруэнтные генераторы ------------------------------------------ #")
print("# ------------------------------------------------------------------------------------- #")
# ГПСЧ - генератор псевдослучайных чисел
# ЛКГ - линейный конгруэнтный генератор
# следующие = (предыдущее * n1 + n2) mod n3
#

def next_random(previous, n1, n2, n3):
    the_next = (previous * n1 + n2) % n3
    return (the_next)

def list_random(n1, n2, n3):
    output = [1]
    while len(output) <= n3:
        output.append(next_random(output[len(output) - 1], n1, n2, n3))

    return (output)

print(list_random(1, 2, 24))
print(list_random(29, 23, 32))
print(list_random(1, 1, 37))

def overlapping_sums(the_list, sum_length):
    length_of_list = len(the_list)
    the_list.extend(the_list)
    output = []
    for n in range(0, length_of_list):
        output.append(sum(the_list[n: (n + sum_length)]))
    return (output)

import matplotlib.pyplot as plt
overlap = overlapping_sums(list_random(211111, 111112, 300007), 12)
plt.hist(overlap, 20, facecolor = 'blue', alpha = 0.5)

plt.title('Result of the Overlapping Sums Test')
plt.xlabel('Sum of Elements of Overlapping Consecutive Sections of List')
plt.ylabel('Frequency of Sum')

# plt.show()

print("# ------------------------------------------------------------------------------------- #")

bits = [1, 1, 1]
print(bits)
xor_result = (bits[1] + bits[2]) % 2
print(xor_result)
output = bits.pop()
print(output)

bits.insert(0, xor_result)
print(bits)








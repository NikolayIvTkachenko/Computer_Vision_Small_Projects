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











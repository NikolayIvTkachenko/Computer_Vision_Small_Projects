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


import math

def revenue(tax):
    return (100 * (math.log(tax+1) - (tax - 0.2)**2 + 0.04))

import matplotlib.pyplot as plt

xs = [x/1000 for x in range(1001)]
ys = [revenue(x) for x in xs]

plt.plot(xs, ys)

current_rate = 0.7
plt.plot(current_rate, revenue(current_rate), 'ro')

plt.title('Tax Rates and Revenues')
plt.xlabel('Tax Rate')
plt.ylabel('Revenue')

# plt.show()

def revenue_derivative(tax):
    return (100 * (1/(tax + 1) - 2 * (tax - 0.2)))

print(revenue_derivative(0.7))

step_size = 0.001

current_rate = current_rate + step_size * revenue_derivative(current_rate)

print("===Реализация градиентного подъема ")
threshold = 0.0001
maximum_iterations = 100000

keep_going = True
iterations = 0

while(keep_going):
    rate_change = step_size * revenue_derivative(current_rate)
    current_rate = current_rate + rate_change

    if(abs(rate_change) < threshold):
        keep_going = False

    if(iterations >= maximum_iterations):
        keep_going = False

    iterations = iterations + 1

print(current_rate)
print(rate_change)





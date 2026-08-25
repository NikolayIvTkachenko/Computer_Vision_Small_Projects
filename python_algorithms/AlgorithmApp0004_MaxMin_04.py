
import math
import matplotlib.pyplot as plt

def revenue(tax):
    return (100 * (math.log(tax+1) - (tax - 0.2)**2 + 0.04))

def revenue_derivative(tax):
    return (100 * (1/(tax + 1) - 2 * (tax - 0.2)))

def revenue_flipped(tax):
    return(0 - revenue(tax))

def revenue_derivative_flipped(tax):
    return (0 - revenue_derivative(tax))

xs = [x/1000 for x in range(1001)]
ys = [revenue_flipped(x) for x in xs]

plt.plot(xs, ys)
plt.title('The Tax/Revenue Curve - Flipped')

plt.xlabel('Current Tax Rate')
plt.ylabel('Revenue - Flipped')

#plt.show()

step_size = 0.001

threshold = 0.0001
maximum_iterations = 10000

current_rate = 0.7
keep_going = True
iterations = 0

rate_change = 0
current_rate = 0

while(keep_going):
    rate_change = step_size * revenue_derivative_flipped(current_rate)
    current_rate = current_rate - rate_change

    if (abs(rate_change) < threshold):
        keep_going = False

    if (iterations >= maximum_iterations):
        keep_going = False

    iterations = iterations + 1

print(current_rate)
print(rate_change)


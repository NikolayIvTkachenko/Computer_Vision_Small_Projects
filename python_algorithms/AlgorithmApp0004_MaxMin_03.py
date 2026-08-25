import math
import matplotlib.pyplot as plt

def income_derivative(edu_yrs):
    return (math.cos((edu_yrs - 10.6) * (2 * math.pi/4)) + 1/2)

threshold = 0.0001
maximum_iterations = 100000

current_education = 12.5
step_size = 0.001

keep_going = True
iterations = 0

rate_change = 0
current_rate = 0

while(keep_going):
    rate_change = step_size * income_derivative(current_rate)
    current_rate = current_rate + rate_change

    if(abs(rate_change) < threshold):
        keep_going = False

    if(iterations >= maximum_iterations):
        keep_going = False

    iterations = iterations + 1

print(current_rate)
print(rate_change)
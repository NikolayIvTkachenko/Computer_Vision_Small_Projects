# Задача комивояжора

import numpy as np
random_seed = 1729
np.random.seed(random_seed)
N = 40

x = np.random.rand(N)
y = np.random.rand(N)

points = zip(x, y)
cities = list(points)

itinerary = list(range(0, N))

print(itinerary)

lines = []

for j in range(0, len(itinerary) - 1):
    lines.append([cities[itinerary[j]], cities[itinerary[j + 1]]])

print(lines)
print(lines[0])

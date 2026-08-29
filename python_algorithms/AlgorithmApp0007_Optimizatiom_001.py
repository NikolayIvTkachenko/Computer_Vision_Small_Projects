# Задача комивояжора
import math
import numpy as np
import matplotlib.collections as mc
import matplotlib.pylab as pl

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

def genlines(cities, itinerary):
    lines = []
    for j in range(0, len(itinerary) - 1):
        lines.append([cities[itinerary[j]], cities[itinerary[j + 1]]])
    return (lines)

def howfar(lines):
    distance = 0
    for j in range(0, len(lines)):
        distance += math.sqrt(abs(lines[j][1][0] - lines[j][0][0])**2 + abs(lines[j][1][1] - lines[j][0][1])**2)
    return (distance)

totaldistance = howfar(genlines(cities, itinerary))
print(totaldistance)

def plotitineary(cities, itin, plottitle, thename):
    lc = mc.LineCollection(genlines(cities, itin), linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0, 1)

    pl.scatter(x, y)
    pl.title(plottitle)

    pl.xlabel('X Coordinate')
    pl.ylabel('Y Coordinate')

    pl.savefig(str(thename) + '.png')
    pl.close()

# cities - список городов
# itin - маршрут, котрый хотим нанести на диагрумма
# plottitle - заголовок
# thename - имя фалйа

plotitineary(cities=cities, itin=itinerary, plottitle='TSP', thename='figure005')

#======================================================
print("========= Реализация поиска ближайшео соседа ==============")
point = [0.5, 0.5]
j = 10
distance = math.sqrt((point[0] - cities[j][0])**2 + (point[1] - cities[j][1])**2)

def findnearest(cities, idx, nnitinerary):
    point = cities[idx]
    mindistance = float('inf')
    minidx = -1

    for j in range(0, len(cities)):
        distance = math.sqrt((point[0] - cities[j][0])**2 + (point[1] - cities[j][1])**2)

        if distance < mindistance and distance > 0 and j not in nnitinerary:
            mindistance = distance
            minidx = j
    return (minidx)

# Выбираем первый город с котороо начинается путешествие



def donn(cities, N):
    nnitinerary = [0]
    for j in range(0, N - 1):
        next = findnearest(cities=cities, idx=nnitinerary[len(nnitinerary) - 1], nnitinerary= nnitinerary)
        nnitinerary.append(next)
    return (nnitinerary)

plotitineary(cities=cities, itin=donn(cities=cities, N=N), plottitle='TSP', thename='figure3')
print(howfar(genlines(cities=cities, itinerary=donn(cities=cities, N=N))))

# =====================================
# Функция, которая вносит небольшие изменния в маршрут, сравнивает измененный маршрут с исходными и возвращает более короткий маршрут
#
print("=================================")









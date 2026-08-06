# https://go.prosv.ru/german-credit-data

import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

trans_set = pd.read_csv('germat_credit.csv', sep=',', header=None) #header=None header=0
data = trans_set.values

# print(data)
clean_data = data[1:, :]

# x = data[:, 2]
# y = data[:, 13]
# z = data[:, 20]
x = clean_data[:, 2].astype(float)
y = clean_data[:, 13].astype(float)
z = clean_data[:, 20].astype(float)

def scatter3d(x, y, z, c):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=c)
    ax.set_title('Кредиты')
    ax.set_xlabel('Длительность кредита (мес.)')
    ax.set_ylabel('Возраст (лет)')
    ax.set_zlabel('Иностранец (нет/да)')

    ax.set_xscale('linear')
    ax.set_yscale('linear')
    ax.set_zscale('linear')

    plt.show()


scatter3d(x, y, z, 'blue')

clients = clean_data
clients = np.delete(clients, np.s_[0:2], axis=1)
clients = np.delete(clients, np.s_[1:11], axis=1)
clients = np.delete(clients, np.s_[2:8], axis=1)

kmeans = KMeans(n_clusters=5, random_state=0).fit(clients)
portraits = kmeans.cluster_centers_

for x in range (5):
    if (round(portraits[x][2])==1):
        resident = 'Гражданин'
    else:
        resident = 'Иностранец'
    months = int(round(portraits[x][0]))
    years = round((months/12), 1)

    print(resident + 'в возрасте ' + str(int(round(portraits[x][1]))) + ' лет и кредит на срок ' + str(months) + ' месяцев (' + str(years) + ') лет.')

# clean_data
kmeans = KMeans(n_clusters=5, random_state=0).fit(clients)
labels = kmeans.labels_
print(labels)
color = list(range(len(data)))

for x in range(len(data)):
    if labels[x] == 0:
        color[x] = 'red'
    elif labels[x] == 1:
        color[x] = 'yellow'
    elif labels[x] == 2:
        color[x] = 'green'
    elif labels[x] == 3:
        color[x] = 'blue'
    else:
        color[x] = 'black'

x = clients[:, 0]
y = clients[:, 1]
z = clients[:, 2]



scatter3d(x, y, z, c=labels)


#=========================================================
# Пример кода

for n_cluster in range(2, 16):
    kmeans = KMeans(n_clusters=n_cluster).fit(clients)
    label = kmeans.labels_
    sil_coeff = silhouette_score(clients, label, metric='euclidean')
    print("Для { } кластеров коэфицентов функции сидуэта = { }.".format(n_cluster, round(sil_coeff, 3)))

# kmeans = KMeans(n_clusters=5, random_state=0).fit(clean_data)
# color = list(range(len(clients)))
# for x in range(len(clients)):
#x = clean_data[:, 0]
#y = clean_data[:, 1]
#z = clean_data[:, 2]






#ValueError: could not convert string to float: 'Duration of Credit (month)'
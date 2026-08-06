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




#ValueError: could not convert string to float: 'Duration of Credit (month)'
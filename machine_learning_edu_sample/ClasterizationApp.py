from sklearn.cluster import KMeans
import pandas as pd

trans_set = pd.read_csv('store_data_01.csv', sep=',', header=None)
X=trans_set.values

print(f"X => {X}")

kmeans = KMeans(n_clusters=3, random_state=0).fit(trans_set)
print(kmeans.labels_)
print(kmeans.cluster_centers_)

for i, kmeans.labels_ in enumerate (kmeans.labels_):
    print("Существо №", i+1, 'относится к типу', kmeans.labels_)

import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

trans_set = pd.read_csv('class_group.csv', sep=',', header=0)
gender = trans_set.values[:, 0]
sportHobby = trans_set.values[:, 1]
belovedSubject = trans_set.values[:, 2]
difficultSubject = trans_set.values[:, 3]
sleepCycle = trans_set.values[:, 4]
group = trans_set.values[:, 5]

print(f"================")
print(f"gender = {gender}")
print(f"sportHobby = {sportHobby}")
print(f"belovedSubject = {belovedSubject}")
print(f"difficultSubject = {difficultSubject}")
print(f"sleepCycle = {sleepCycle}")
print(f"group = {group}")
print(f"================")

enc = preprocessing.LabelEncoder()

gender_encoded = enc.fit_transform(gender)
sportHobby_encoded = enc.fit_transform(sportHobby)
belovedSubject_encoded = enc.fit_transform(belovedSubject)
difficultSubject_encoded = enc.fit_transform(difficultSubject)
sleepCycle_encoded = enc.fit_transform(sleepCycle)
group_encoded = enc.fit_transform(group)
print(f"================")
print(f"gender_encoded = {gender_encoded}")
print(f"sportHobby_encoded = {sportHobby_encoded}")
print(f"belovedSubject_encoded = {belovedSubject_encoded}")
print(f"difficultSubject_encoded = {difficultSubject_encoded}")
print(f"sleepCycle_encoded = {sleepCycle_encoded}")
print(f"group_encoded = {group_encoded}")
print(f"================")

X = list(zip(gender_encoded, sportHobby_encoded, belovedSubject_encoded, difficultSubject_encoded, sleepCycle_encoded))
Y = group_encoded
print(f"================")
print(f"X => {X}")
print(f"Y => {Y}")
print(f"================")

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, Y)

gender_dict = dict()
sportHobby_dict = dict()
belovedSubject_dict = dict()
difficultSubject_dict = dict()
sleepCycle_dict = dict()
group_dict = dict()
print(f"================")
print(f"gender_dict => {gender_dict}")
print(f"sportHobby_dict => {sportHobby_dict}")
print(f"belovedSubject_dict => {belovedSubject_dict}")
print(f"difficultSubject_dict => {difficultSubject_dict}")
print(f"sleepCycle_dict => {sleepCycle_dict}")
print(f"group_dict => {group_dict}")
print(f"================")

for i in range (len(gender_encoded)):
    gender_dict[gender[i]] = gender_encoded[i]

for i in range (len(sportHobby)):
    sportHobby_dict[sportHobby[i]] = sportHobby_encoded[i]

for i in range (len(belovedSubject)):
    belovedSubject_dict[belovedSubject[i]] = belovedSubject_encoded[i]

for i in range (len(difficultSubject)):
    difficultSubject_dict[difficultSubject[i]] = difficultSubject_encoded[i]

for i in range (len(sleepCycle)):
    sleepCycle_dict[sleepCycle[i]] = sleepCycle_encoded[i]

for i in range (len(group)):
    group_dict[group[i]] = group_encoded[i]
print(f"================================")
print(f"============ AFTER =============")
print(f"gender_dict => {gender_dict}")
print(f"sportHobby_dict => {sportHobby_dict}")
print(f"belovedSubject_dict => {belovedSubject_dict}")
print(f"difficultSubject_dict => {difficultSubject_dict}")
print(f"sleepCycle_dict => {sleepCycle_dict}")
print(f"group_dict => {group_dict}")
print(f"========== END =================")

newOne = knn.predict([[
    gender_dict[input("Какого пола новичок? ")],
    sportHobby_dict[input("Какой вид спорта ему/ей нравится? ")],
    belovedSubject_dict[input("Какой предмет у него/нее любимый? ")],
    difficultSubject_dict[input("Какой предмет для него.нее самый сложный? ")],
    sleepCycle_dict[input("Какой у него/нее режим сна? ")]
]])

print(f"Скорее всего, он будет дружить с группой: {list(group_dict.keys())[list(group_dict.values()).index(newOne)]} ")





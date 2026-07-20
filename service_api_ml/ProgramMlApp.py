import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

# Заголовки в файле itanic.csv
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

data = pd.read_csv('titanic.csv')
data = data[['Survived', 'Pclass', 'Age', 'Fare']]
data = data.dropna(subset=['Age'])

print(data.info())

print(data.Fare.describe())

print(data.drop('Survived', axis=1))

train, test = train_test_split(data, test_size=0.2)


import matplotlib.pyplot as plt
import numpy as np
import itertools

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues): #Blues
    #pip install matplotlib --upgrade
    """
    Функция для построения матрицы ошибок.
    cm - матрица ошибок
    classes - список классов
    normalize - если True, то значения матрицы ошибок нормализуются к 1
    title - заголовок графика
    cmap - цветовая схема для отображения графика
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix, without normalization")

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel("True label")
    plt.xlabel("Predicted label")

def experiment(max_depth, min_samples_split):
    # Создание и обучение модели решающего дерева
    model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split)
    model.fit(train.drop('Survived', axis=1), train['Survived'])

    # Вычисление метрик
    preds = model.predict(test.drop('Survived', axis=1))
    acc = accuracy_score(test['Survived'], preds)
    cm = confusion_matrix(test['Survived'], preds)

    print("accuracy", acc)

    # Визуализация матрицы ошибок
    plot_confusion_matrix(cm, classes=['Not Survived', 'Survived'])

    # Вывод
    report = classification_report(test['Survived'], preds, target_names=['Not Survived', 'Survived'])
    print(report)

    # Сохранение модели в формате pickle
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

# Определение гиперпараметров модели
max_depth = 5
min_sample_split = 150

experiment(max_depth, min_sample_split)



# Проверка работы модели

import pickle
import pandas as pd

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

new_data = pd.DataFrame({
    'Pclass': [3],
    'Age': [22.0],
    'Fare': [7.2500]
})

# Предскаание
predictions = model.predict(new_data)

# Вывод результатов
print("Predicted Survival:", predictions)

# TEST API



















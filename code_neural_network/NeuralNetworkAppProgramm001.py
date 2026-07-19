# Google Colab

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
# %matplotlib inline — только для интерактивных сред (Jupyter

#from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import utils

fashion_mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

plt.figure()
plt.imshow(x_train[0])
plt.colorbar()
plt.grid(False)

#Нормализация данных
x_train = x_train / 255
x_test = x_test / 255

plt.figure()
plt.imshow(x_train[0])
plt.colorbar()
plt.grid(False)

# Отопразим несколько моделей
plt.figure(figsize=(10, 10))
for i in range (25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x_train[i])
    plt.xlabel(class_names[y_train[i]])

# Создаем модели нейронной сети
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer=tf.keras.optimizers.SGD(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary()

model.fit(x_train, y_train, epochs=10)


# Проверка точности предсказания
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accurancy: ", test_acc)

predictions = model.predict(x_train)
print(predictions[0])

# Индекс максимального значения
print(np.argmax(predictions[0]))
# Выведем правильный ответ из меток для тестирования
print(y_train[0])

print(y_train[12])

plt.figure()
plt.imshow(x_train[12])
plt.colorbar()
plt.grid(False)

# Показать название класса
print(class_names[np.argmax(predictions[12])])

#=====================================================================
#https://www.youtube.com/watch?v=8mkh4uGxNfo




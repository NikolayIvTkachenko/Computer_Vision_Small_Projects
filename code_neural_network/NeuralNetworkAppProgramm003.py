# Сверточная нейронная сеть для распознования кошек и собак
# pip install tensorflow_datasets

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras
from matplotlib import pyplot as plt


def preprocess(img, label):
    return tf.image.resize(img, [200, 200]) / 255, label


split = ["train[:70%]", "train[70:]"]

trainDatasets, testDatasets = tfds.load(name='cats_vs_dogs', split=split, as_supervised=True)

# Загрузка датасет на несколько партий/пакетов (batch)
trainDatasets = trainDatasets.map(preprocess).batch(32)
testDatasets = testDatasets.map(preprocess).batch(32)

model = keras.Sequential([
    keras.layers.Conv2D(16, (3, 3), activision='relu', input_shape=(200, 200, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(32, (3, 3), activision='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activision='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
trainHistory = model.fit(trainDatasets, epoch=10, validation_data=testDatasets)

plt.plot(trainHistory.history['accuracy'])
plt.plot(trainHistory.history['val_accuracy'])
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'])
plt.grid()

plt.show()

(loss, accuracy) = model.evaluate(testDatasets)
print(loss)
print(accuracy)

# Сохраняем модель
model.save("model1.h5")

#trainDatasets, testDatasets = tfds.load(name='cats_vs_dogs', split=split, as_supervised=True)
#KeyError: "There is no item named 'PetImages\\\\Cat\\\\0.jpg' in the archive"
#https://github.com/tensorflow/tensorflow/issues/84104









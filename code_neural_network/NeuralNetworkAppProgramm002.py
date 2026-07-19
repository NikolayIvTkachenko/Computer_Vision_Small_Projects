import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_label), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(256, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', loss="sparse_categorical_crossentropy", metrics=['accuracy'])
model.fit(train_images, train_label, epochs=20)

model.evaluate(test_images, test_labels)

predictions = model.predict(test_images)

print(predictions[0])
print(test_labels[0])

plt.imshow(test_images[0])
plt.show()
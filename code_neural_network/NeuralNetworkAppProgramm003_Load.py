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

classNames = ['cat', 'dog']

model = keras.models.load_model("model1.h5")

predictions = model.predict(testDatasets.take(8))

i = 0
fig, ax = plt.subplots(1, 8)
for image, _ in testDatasets.take(8):
    predictedLabel = int(predictions[i] >= 0.5)
    ax[i].axis('off')
    ax[i].set_title(classNames[predictedLabel])
    ax[i].imshow(image[0])
    i += 1

plt.show()
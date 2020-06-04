# 1. Introductory example

import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape = (28, 28)),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation = 'softmax')
    ])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

model.evaluate(x_test, y_test)

model.save("mnist3poch.h5")
loaded = tf.keras.models.load_model("mnist3poch.h5")

where = 200
predictions = loaded.predict(x_test[where : where+5])
print(predictions[0])
print(" - meaning - " + str(np.argmax(predictions[0])))

plt.imshow(x_test[where], cmap=plt.cm.binary)
plt.xlabel("Prediction: " + str(np.argmax(predictions[0])))
plt.show()
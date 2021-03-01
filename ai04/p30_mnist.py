from tensorflow.examples.tutorials.mnist.input_data import read_data_sets
import cv2   # opencv-python
import numpy as np


dss = read_data_sets('../../../../codes/qrz/samples/MNIST_data')
print(dss.train.num_examples)
print(dss.train.next_batch)
print(dss.validation.num_examples)
print(dss.test.num_examples)


imgs, labels = dss.train.next_batch(100)  # imgs: [100, 28*28], labels: [10]

print(labels)
# np.reshape(), np.transpose()
cols = 10
imgs = np.reshape(imgs, [-1, cols, 28, 28])
imgs[:, :, 27, :] = 1.0
imgs[:, :, :, 0] = 1.0
imgs = np.transpose(imgs, [0, 2, 1, 3])  # [-1, 28, 10, 28]
img = np.reshape(imgs, [-1, 28 * cols]) # [280, 280]
img[0, :] = 1.0
img[:, -1] = 1.0
cv2.imshow('My image', img)
cv2.waitKey()


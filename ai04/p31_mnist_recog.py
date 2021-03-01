from tensorflow.examples.tutorials.mnist.input_data import read_data_sets
import tensorflow as tf
import numpy as np
import time


class Tensors:
    def __init__(self, mid_units=2000):
        """
        the member variables: img, label, train_op, lr, predict
        """
        self.img = tf.placeholder(tf.float32, [None, 784], 'img')
        self.label = tf.placeholder(tf.int32, [None], 'label')
        self.lr = tf.placeholder(tf.float32, [], 'lr')

        # matmul(), +
        t = tf.layers.dense(self.img, mid_units, activation=tf.nn.relu)  # [-1, mid_units]
        # t = tf.nn.relu(t)
        t = tf.layers.dense(t, 10)  # [-1, 10]
        self.predict = tf.argmax(t, axis=1)
        p = tf.nn.softmax(t)

        label = tf.one_hot(self.label, 10)  # [-1, 10]
        loss = tf.reduce_mean(tf.square(p - label))  # (p-label)**2
        opt = tf.train.AdamOptimizer(self.lr)

        self.train_op = opt.minimize(loss)


class Model:
    def __init__(self, session, lr=0.001, batch_size=200, epoches=50):
        self.lr = lr
        self.batch_size = batch_size
        self.epoches = epoches
        self.tensors = Tensors()
        self.session = session
        self.dss = read_data_sets('MNIST_data')

    def train(self):
        print('Training is started!')
        batches = self.dss.train.num_examples // self.batch_size
        ts = self.tensors
        self.session.run(tf.global_variables_initializer())
        for epoch in range(self.epoches):
            for batch in range(batches):
                imgs, labels = self.dss.train.next_batch(self.batch_size)  # imgs: [bs, 784], labels:[bs]
                self.session.run(ts.train_op, {ts.lr: self.lr, ts.img: imgs, ts.label: labels})
            print('epoch %d finished.' % epoch)
        print('Training is finished!')

    def test(self):
        pass


if __name__ == '__main__':
    start = time.time()
    with tf.Session() as session:
        model = Model(session)
        model.train()
        model.test()
    end = time.time()
    print("Running time: {}seconds".format(end - start))

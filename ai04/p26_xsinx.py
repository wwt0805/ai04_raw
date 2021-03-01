import tensorflow as tf

x1 = tf.get_variable('x1', [], tf.float32, tf.initializers.ones)
x2 = tf.get_variable('x2', [], tf.float32, tf.initializers.ones)
y = (x1 + 3) ** 2 + (x2 - 1) ** 2

lr = tf.placeholder(tf.float32, [], 'lr')
opt = tf.train.GradientDescentOptimizer(lr)
train_op = opt.minimize(y)
session = tf.Session()
session.run(tf.global_variables_initializer())

def solve(lr_v=0.001, epoches=2000):
    for _ in range(epoches):
        session.run(train_op, {lr:lr_v})
    return session.run([x1, x2])


def main():
    with session:
        print(solve(epoches=10000))

main()
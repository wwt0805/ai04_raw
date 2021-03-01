import tensorflow as tf

x = tf.get_variable('x1', [], tf.float32, tf.initializers.ones) * 6
y = (x * tf.sin(x) - 3) ** 2

lr = tf.placeholder(tf.float32, [], 'lr')
opt = tf.train.AdamOptimizer(lr)
train_op = opt.minimize(y)
session = tf.Session()
session.run(tf.global_variables_initializer())

def solve(lr_v=0.001, epoches=5000):
    for _ in range(epoches):
        session.run(train_op, {lr:lr_v})
    return session.run(x)


def main():
    with session:
        print(solve(epoches=2000))

main()
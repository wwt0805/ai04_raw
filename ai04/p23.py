# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior

import tensorflow as tf
import numpy as np

c1 = tf.constant([[2, 3], [1, 4], [5, -1]])   # === exp.Const(3)
print(c1)

v1 = tf.get_variable('aaa', [], tf.float32, tf.initializers.ones)  # v2 === exp.Variable('aaa')
print(v1)

v3 = v1 * 327  # === exp.Mul(v1, Const(327)),  Broadcasting
# v2.eval({v2:123})

with tf.Session() as session:
    # session.run(tf.global_variables_initializer())
    print(session.run([c1, v3], {v1:1000}))   # === c1.eval({})

# session = tf.Session();
# session.open();
# try {
#     print(session.run(c1))
# } finally {
#     session.close()
# }

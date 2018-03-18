import tensorflow as tf
import numpy as np

# # 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# # 加到默认图中.
# #
# # 构造器的返回值代表该常量 op 的返回值.
# matrix1 = tf.constant([[3., 3.]])
#
# # 创建另外一个常量 op, 产生一个 2x1 矩阵.
# matrix2 = tf.constant([[2.],[2.]])
#
# # 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# # 返回值 'product' 代表矩阵乘法的结果.
# product = tf.matmul(matrix1, matrix2)
#
# sess = tf.Session()
#
# print(sess.run(product))

# placeholder and variable============================================
# a = tf.placeholder(tf.int16)
# b = tf.placeholder(tf.int16)
#
# add = tf.add(a, b)
# mul = tf.multiply(a, b)
#
# with tf.Session() as sess:
#     with tf.device('/cpu:0'):
#         print(sess.run(add, feed_dict={a: 2, b: 3}))
#         print(sess.run(mul, feed_dict={a:2 , b: 3}))
#
# c = tf.Variable(tf.ones([2, 3]))
# d = tf.Variable(tf.ones([3, 2]))
# p = tf.matmul(2*d, 5*c)
#
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)
# print(sess.run(p))

# =====================================counter
# state = tf.Variable(0, name='counter')
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
#
# init_op = tf.global_variables_initializer()
#
# with tf.Session() as sess:
#     sess.run(init_op)
#     print(sess.run(state))
#     for _ in range(5):
#         sess.run(update)
#         print(sess.run(state))
#
# # =====================================ML——use train
# W = tf.Variable([.3], tf.float32)
# b = tf.Variable([-.3], tf.float32)
# x = tf.placeholder(tf.float32)
# y = tf.placeholder(tf.float32)
#
# linear_model = W * x + b
#
# square_deltas = tf.square(linear_model - y)
# loss = tf.reduce_sum(square_deltas)
#
# # fixW = tf.assign(W, [-1.])
# # fixb = tf.assign(b, [1.])
#
# optimizer = tf.train.GradientDescentOptimizer(0.01)
# train = optimizer.minimize(loss)
#
# x_train = [1, 2, 3, 4]
# y_train = [0, -1, -2, -3]
#
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)
# for i in range(1000):
#     sess.run(train, feed_dict={x: x_train, y: y_train})
#     if i % 50 == 0:
#         print('train_step: %d -----ok'%(i))
# curr_W, curr_b, curr_loss = sess.run([W, b, loss], feed_dict={x: x_train, y: y_train})
# print('W: %s  b: %s  loss: %s'%(curr_W, curr_b, curr_loss))
# # sess.run(fixb)
# # sess.run(fixW)
#
# # print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))


# # ======================================================use tf.contrib.learn
# features = [tf.contrib.layers.real_valued_column('x', dimension=1)]
# estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)
# x = np.array([1, 2, 3, 4])
# y = np.array([0, -1, -2, -3])
# input_fn = tf.contrib.learn.io.numpy_input_fn({'x': x}, y, batch_size=4, num_epochs=1000)
# estimator.fit(input_fn=input_fn, steps=1000)
#
# print(estimator.evaluate(input_fn=input_fn))

# =========================================================custom model
def model(features, labels, mode):
    W = tf.get_variable('W', [1], dtype=tf.float64)
    b = tf.get_variable('b', [1], dtype=tf.float64)

    y = W * features['x'] + b

    loss = tf.reduce_mean(tf.square(y - labels))
    global_step = tf.train.get_global_step()
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = tf.group(optimizer.minimize(loss), tf.assign_add(global_step, 1))
    return tf.contrib.learn.ModelFnOps(mode=mode,
                                       loss=loss,
                                       train_op=train)

estimator = tf.contrib.learn.Estimator(model_fn=model)

# define data set
x = np.array([1, 2, 3, 4])
y = np.array([0, -1, -2, -3])
input_fn = tf.contrib.learn.io.numpy_input_fn({'x': x}, y, 4, num_epochs=1000)

# train
estimator.fit(input_fn=input_fn, steps=1000)

# evaluate
print(estimator.evaluate(input_fn=input_fn, steps=10))




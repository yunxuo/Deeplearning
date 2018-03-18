import tensorflow as tf
import numpy as np

#creat phony data 100 points
x_data = np.float32(np.random.rand(2, 100))
y_data = np.dot([0.100, 0.200], x_data) + 0.300

#model
w = tf.Variable(tf.random_uniform([1,2], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = tf.matmul(w, x_data) + b


loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for step in range(0,201):
    sess.run(train)
    print(step, sess.run(w), sess.run(b))
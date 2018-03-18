from tensorflow.contrib.learn.python.learn.datasets.mnist import *
import input_data
import tensorflow as tf
import os
from mnist_demo import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#get data
filename = 'train-images-idx3-ubyte.gz'
if not os.path.exists(filename):
    mnist_data = read_data_sets('mnist_data/', one_hot=True)

#input data
x = tf.placeholder(tf.float32, [None, 784])

#weight & bias
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros(10))

#models
y = tf.matmul(x, w) + b

y_ = tf.placeholder(tf.float32, [None, 10])

# cross_entropy = -tf.reduce_sum(y_*tf.log(y))
# # cross_entropy = -tf.reduce_sum(y * tf.log(y_) + (1 - y) * tf.log(1 - y_))
cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(5000):
    batch_xs, batch_ys = mnist_data.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

result = sess.run(accuracy, feed_dict={x: mnist_data.test.images, y_: mnist_data.test.labels})

print(result)
print(sess.run(b))

# test Image--------------------------------------------------------
# dir_name="test_num"
# files = os.listdir(dir_name)
# cnt=len(files)
# for i in range(cnt):
#   files[i]=dir_name+"/"+files[i]
#   # print(files[i])
#   test_images1,test_labels1=GetImage([files[i]])
#   # print (tf.cast(correct_prediction, tf.float32).eval)
#   # print(shape(test_images1))
#   mnist_data.test = DataSet(test_images1, test_labels1, dtype=tf.float32)
#   res=accuracy.eval({x: mnist_data.test.images, y_: mnist_data.test.labels})
#
#   # print(shape(mnist.test.images))
#   # print (tf.argmax(y, 1))
#   # print(y.eval())
#   print("output:",int(res[0]))
#   print("\n")
#

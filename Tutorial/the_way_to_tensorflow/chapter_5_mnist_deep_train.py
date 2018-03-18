import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets("mnist_data/", one_hot=True)     #下载并加载mnist数据


x = tf.placeholder(tf.float32, [None, 784])                        #输入的数据占位符
y_actual = tf.placeholder(tf.float32, shape=[None, 10])            #输入的标签占位符

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME')

# 接下来构建网络。
# 整个网络由两个卷积层（包含激活层和池化层），
# 一个全连接层，一个dropout层和一个softmax层组成。
#
# 第一个卷积层：
# The convolution will compute 32 features for each 5x5 patch.
# Its weight tensor will have a shape of [5, 5, 1, 32].
# The first two dimensions are the patch size,
# the next is the number of input channels,
# and the last is the number of output channels.
#
# w和b有多少组，卷积层结束后就输出多少层features map，
# 也就是这里的output channels。一组w和b对应着一种卷积核，
# 不同卷积核代表着关注的特征类别不同，用每种卷积核运算之后会得到一层特征图。

# 在创建第一个卷积层之前，我们需要将输入数据x reshape成一个4维张量，
# 其中的第2/3维对应着图像的width和height，
# 最后一维对应着the number of color channels.
x_image = tf.reshape(x, [-1,28,28,1])         #转换输入数据shape,以便于用于网络中
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

# convolve x_image with the weight tensor,add the bias,
# apply the ReLU function, and finally max pool.The max_pool_2x2 method
# will reduce the image size to 14x14.

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)     #第一个卷积层
h_pool1 = max_pool(h_conv1)                                  #第一个池化层

# In order to build a deep network, we stack several layers of this type.
#  The second layer will have 64 features for each 5x5 patch

W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)      #第二个卷积层
h_pool2 = max_pool(h_conv2)                                   #第二个池化层

# Now that the image size has been reduced to 7x7,
#  we add a fully-connected layer with 1024 neurons to allow processing on the
# entire image. We reshape the tensor from the pooling layer into a batch of vectors,
# multiply by a weight matrix, add a bias, and apply the ReLU

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])              #reshape成向量
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)    #第一个全连接层

# To reduce overfitting, we will apply dropout before readout layer.
# We create a placeholder for the probability that a neuron's
# output is kept during dropout.
# This allows us to turn dropout on during training,
# and turn it off during testing.
# TensorFlow's tf.nn.dropout op automatically handles scaling neuron outputs
# in addition to masking them , so dropout just works without any additional scaling.

keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)                  #dropout层

#Finally,we add a layer,just like for the one layer softmax regression above.

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_predict=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)   #softmax层

# 网络构建好后，就可以开始训练了。
#
# 大体和softmax模型一样。主要不同在于：
#
# 1·我们用更复杂的ADAM 优化器 取代了梯度下降。
#
# 2·我们在feed_dict部分添加了额外的参数keep_prob来控制dropout的比率。
#
# 3·我们在训练过程中的每100次迭代，将结果添加到日志。

cross_entropy = -tf.reduce_sum(y_actual*tf.log(y_predict))     #交叉熵
train_step = tf.train.GradientDescentOptimizer(1e-3).minimize(cross_entropy)    #梯度下降法
correct_prediction = tf.equal(tf.argmax(y_predict,1), tf.argmax(y_actual,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))                 #精确度计算
sess=tf.InteractiveSession()
sess.run(tf.initialize_all_variables())
for i in range(20000):
  batch = mnist.train.next_batch(50)
  if i%100 == 0:                  #训练100次，验证一次
    train_acc = accuracy.eval(feed_dict={x:batch[0], y_actual: batch[1], keep_prob: 1.0})
    print('step %d, training accuracy %g' % (i, train_acc))
    train_step.run(feed_dict={x: batch[0], y_actual: batch[1], keep_prob: 0.5})

test_acc=accuracy.eval(feed_dict={x: mnist.test.images, y_actual: mnist.test.labels, keep_prob: 1.0})
print("test accuracy %g" % (test_acc))

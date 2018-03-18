import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# # 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# # 加到默认图中.-------------------------------------------
# #
# # 构造器的返回值代表该常量 op 的返回值.
# matrix1 = tf.constant([[3, 3]])
#
# # 创建另外一个常量 op, 产生一个 2x1 矩阵.
# matrix2 = tf.constant([[2],[2]])
#
# # 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# # 返回值 'product' 代表矩阵乘法的结果.
# product = tf.matmul(matrix1, matrix2)
#
# # sess = tf.Session()
# #
# # print(sess.run(product))
# # #print(product)
# #
# # sess.close()
#
# # 进入一个交互式 TensorFlow 会话.-----------------------
# sess = tf.InteractiveSession()
#
# x = tf.Variable([1.0, 2.0])
# a = tf.constant([3.0, 3.0])
#
# # 使用初始化器 initializer op 的 run() 方法初始化 'x'
# x.initializer.run()
#
# # 增加一个减法 sub op, 从 'x' 减去 'a'. 运行减法 op, 输出结果
# sub = tf.subtract(x, a)
# print(sub.eval())

# 创建一个变量, 初始化为标量 0.------------------------------------
# state = tf.Variable(0, name="counter")
#
# # 创建一个 op, 其作用是使 state 增加 1
#
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
#
# # 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# # 首先必须增加一个`初始化` op 到图中.
# init_op = tf.global_variables_initializer()
#
# # 启动图, 运行 op
# with tf.Session() as sess:
#   # 运行 'init' op
#   sess.run(init_op)
#   # 打印 'state' 的初始值
#   print(sess.run(state))
#   # 运行 op, 更新 'state', 并打印 'state'
#   for i in range(3):
#     sess.run(update)
#     aa = str(i) + ' :'
#     print(aa, sess.run(state))

# Fetch-------------------------------------------------------
# 为了取回操作的输出内容, 可以在使用 Session 对象的 run() 调用
# 执行图时, 传入一些 tensor, 这些 tensor 会帮助你取回结果.
# 在之前的例子里, 我们只取回了单个节点 state, 但是你也可以取回多个 tensor:
# input1 = tf.constant(3.0)
# input2 = tf.constant(2.0)
# input3 = tf.constant(5.0)
#
# intermed = tf.add(input2, input3)
# mul = tf.multiply(input1, intermed)
#
# with tf.Session() as sess:
#     result = sess.run([mul, intermed])
#     print(result)
#
# Feed----------------------------------------------------------------------
# 上述示例在计算图中引入了 tensor, 以常量或变量的形式存储.
# TensorFlow 还提供了 feed 机制, 该机制 可以临时替代图中的
# 任意操作中的 tensor 可以对图中任何操作提交补丁, 直接插入一个 tensor
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run([output], feed_dict={input1: [7], input2: [8]}))



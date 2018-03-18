# 对于机器学习，尤其是深度学习DL的算法，模型训练可能很耗时，
# 几个小时或者几天，所以如果是测试模块出了问题，每次都要重新运行就显得很浪费时间，
# 所以如果训练部分没有问题，那么可以直接将训练的模型保存起来，然后下次运行直接加载模型，
# 然后进行测试很方便。
#
# 在tensorflow中保存（save）和加载（restore）模型的类是tf.train.Saver()，
# 其中变量保存的是key-value，不传参数默认是全部变量。
import tensorflow as tf

# 保存模型使用的是save函数，先创建一个saver对象:===================
# """
# 声明variable和op
# 初始化op声明
# """
# #创建saver对象，它添加了一些op用来save和restore模型参数
# saver = tf.train.Saver()
#
# with tf.Session() as sess:
#     sess.run(init_op)
#     #训练模型过程
#     #使用saver提供的简便方法去调用 save op
#     saver.save(sess, "save_path/file_name.ckpt")

# 加载模型使用的是restore函数，先创建一个saver对象:==========================
# """
# 声明variable和op
# 初始化op声明
# """
# #创建saver 对象
# saver = tf.train.Saver()
#
# with tf.Session() as sess:
#     sess.run(init_op)#可以执行或不执行，restore的值会override初始值
#     saver.restore(sess, "save_path/file_name.ckpt")













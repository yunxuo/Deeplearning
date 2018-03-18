from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('mnist_data', one_hot=True)

print('train_images', mnist.train.images.shape)
print('train_labels', mnist.train.labels.shape)
print(mnist.validation.images.shape)
print(mnist.validation.labels.shape)
print(mnist.test.images.shape)
print(mnist.test.labels.shape)

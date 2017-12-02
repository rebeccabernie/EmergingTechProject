import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# Adapted from https://www.tensorflow.org/get_started/mnist/beginners
# and https://www.tensorflow.org/get_started/mnist/pros

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Weights and biases - learnable params, adjusted towards values that have correct output during training
# Low weight means input won't change output much, low bias generally means it won't learn as fast
# https://datascience.stackexchange.com/questions/19099/what-is-weight-and-bias-in-deep-learning, https://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks
# Variable class allows tensor to be used / modified
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape) # Init bias at small value to avoid dead neurons / 
  return tf.Variable(initial)

# Convolution and pooling - 
# Convolution layers apply specified number (1) of convolution filters to an image
# Pooling layers lower the sample rate/size of the image data extracted by convolution layers, reducing dimensionality which reduces processing time.
def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

#def train():
    # Download MNIST data using input_data.read_data_sets, save it into a folder. 
    # Use one hot encoding (easier to deal with when using machine learning, explained in readme
    #mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

def test():
    print("Test working")
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

# Input layer - nodes for input images and target output classes
x  = tf.placeholder(tf.float32, [None, 784], name='x') # None: batch size, none means any size. 784: flattened 28x28 image, 28 x 28 = 784
y_ = tf.placeholder(tf.float32, [None, 10],  name='y_') # 10 = one hot encoded 10 dimensional image (categories 0-9, OHE explained in README)

# First Convolutional Layer
W_conv1 = weight_variable([5, 5, 1, 32]) # Weight tensor. 5 x 5 patch size, 1 input channel, 32 output channels
b_conv1 = bias_variable([32]) # Bias has a component for each output channel
x_image = tf.reshape(x, [-1, 28, 28, 1]) # Reshape to 4D tensor, 28 width, 28 height, 1 colour channel
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1) # Combine the x_image with the weight tensor, add bias, apply ReLU function (rectified linear unit - if the input is greater than 0, output is equal to initial input)
h_pool1 = max_pool_2x2(h_conv1) # Max pool 2x2 reduces image to 14x14

# Second
W_conv2 = weight_variable([5, 5, 32, 64]) # 5x5 again, 32 inputs (for 32 outputs in 1st layer), 64 outputs - 64 features for each patch
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

#def train():
    # Download MNIST data using input_data.read_data_sets, save it into a folder. 
    # Use one hot encoding (easier to deal with when using machine learning, explained in readme
    #mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

def test():
    print("Test working")
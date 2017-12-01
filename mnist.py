import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# Adapted from https://www.tensorflow.org/get_started/mnist/beginners

def train():
    # Download MNIST data using input_data.read_data_sets, save it into a folder. 
    # Use one hot encoding (easier to deal with when using machine learning, explained in readme
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

    # Placeholder used to allow input of any number of mnist images
    # 784 dimensions (28 x 28), dimensions can be of any length
    x = tf.placeholder(tf.float32, [None, 784]) 

    # Weights and biases - learnable params, adjusted towards values that have correct output during training
    # Low weight means input won't change output much, low bias generally means it won't learn as fast
    # https://datascience.stackexchange.com/questions/19099/what-is-weight-and-bias-in-deep-learning, https://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks
    # Variable class allows tensor to be used / modified
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

    # Create the model
    # Softmax ideal for probabilities, gives a list of values between 0 and 1 (0-100%) that add up to 1 (100%)
    # Matmul function multiplies matrices (mnist and weight)
    y = tf.nn.softmax(tf.matmul(x, W) + b)

    print(y)

def test():
    print("Test working")
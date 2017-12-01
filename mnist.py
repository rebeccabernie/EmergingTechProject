# Adapted from https://www.tensorflow.org/get_started/mnist/beginners

# Download the 
from tensorflow.examples.tutorials.mnist import input_data

# 
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


def test():
    print("Test working")
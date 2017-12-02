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
h_pool2 = max_pool_2x2(h_conv2) # Image size now 7x7

# Densely connected layer (fully connected)
W_fc1 = weight_variable([7 * 7 * 64, 1024]) # 1024 neurons to process whole image 
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64]) # Reshape tensor from pooling layer
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1) # Multiply by weight, add bias, apply ReLU

# Dropout - reduces overfitting
keep_prob = tf.placeholder(tf.float32) # Placeholder for probability that neuron's output is kept duing dropout
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob) # .dropout handles scaling automaticall. h_fc1 tensor, prob that n's output is kept

# Readout - output layer
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

#Add inputs / outputs for saving
tf.add_to_collection("keep_prob", keep_prob)
tf.add_to_collection("x", x)
tf.add_to_collection("y_", y_)
tf.add_to_collection("y_conv", y_conv)

# Evaluate
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy) # Adam optimization with learning rate of 0.0001. Adam used when datasets have a seemingly random pattern, see https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/ for further reading
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Save the model, adapted from http://www.itzikbs.com/tensorflow-deep-mnist-experts-tutorial
saver = tf.train.Saver(max_to_keep=3)
checkpoints = "./checkpoints/mnistmodel" # File will save in checkpoints folder, with prefix. mnistmodel-400

# Train
with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  for i in range(300):
    batch = mnist.train.next_batch(50)
    if i % 100 == 0:
      train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
      print('Step: %d, Accuracy: %g' % (i, train_accuracy))
      saver.save(sess, checkpoints, global_step = i)
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

  print('Test Accuracy: %g' % accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))

#def train():
    # Download MNIST data using input_data.read_data_sets, save it into a folder. 
    # Use one hot encoding (easier to deal with when using machine learning, explained in readme
    #mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

def test():
    print("Test working")
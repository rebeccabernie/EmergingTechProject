import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

checkpointsDir = "./checkpoints/"
model = "mnistmodel"

sess = tf.Session()
newSaver = tf.train.import_meta_graph(checkpointsDir + model + ".meta")
newSaver.restore(sess, checkpointsDir + model)

keep_prob = tf.get_collection("keep_prob")[0]
x = tf.get_collection("x")[0]
y_ = tf.get_collection("y_")[0]
y_conv = tf.get_collection("y_conv")[0]

inputInd = 4
testImg = mnist.test.images[inputInd].reshape(1, 784)
actual = mnist.test.labels[inputInd].reshape(1, 10)

logit = sess.run(y_conv,feed_dict={ x: testImg, y_: actual, keep_prob: 1.0})
prediction = sess.run(tf.argmax(logit,1))
digit = sess.run(tf.argmax(actual,1))
print("Prediction : %d, Actual : %d"% (prediction, digit))
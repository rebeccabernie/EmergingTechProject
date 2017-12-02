import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
import numpy as np

# Adapted from http://www.itzikbs.com/tensorflow-deep-mnist-experts-tutorial / https://github.com/sitzikbs/TensorFlow-Tutorials/blob/master/ImportModel.py

# Checkpoints folder and model file
checkpointsDir = "./checkpoints/"
model = "mnistmodel"

sess = tf.Session()
# Recreate the graph saved in the folder
newSaver = tf.train.import_meta_graph(checkpointsDir + model + ".meta")
newSaver.restore(sess, checkpointsDir + model)

# Reload the saved variables
keep_prob = tf.get_collection("keep_prob")[0]
x = tf.get_collection("x")[0]
y_ = tf.get_collection("y_")[0]
y_conv = tf.get_collection("y_conv")[0]

# Test the saved model, 4th image in the dataset is a 4
inputInd = 4
testImg = mnist.test.images[inputInd].reshape(1, 784)
actual = mnist.test.labels[inputInd].reshape(1, 10)

logit = sess.run(y_conv, feed_dict={x: testImg, y_: actual, keep_prob: 1.0})
prediction = sess.run(tf.argmax(logit, 1))
digit = sess.run(tf.argmax(actual, 1))
print("Prediction : %d, Actual : %d"% (prediction, digit))

def predict(image):
    # Flatten the image into one dimension
    imgArr = np.ndarray.flatten(np.array(image)).reshape(1, 784)

    prediction = tf.argmax(y_conv,1)
    print("Prediction: {}".format(prediction.eval(feed_dict={x:imgArr, keep_prob:1.0}, session=sess)))
    return prediction.eval(feed_dict={x:imgArr, keep_prob:1.0}, session=sess)
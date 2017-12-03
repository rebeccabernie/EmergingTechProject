# Digit Recogniser Project

> Student: Rebecca Kane, G00320698  

> Module: Emerging Technologies / 4th Year   
> Lecturer: Dr Ian McLoughlin  
> [Project Specification](https://emerging-technologies.github.io/problems/project.html)  

This project is a web application that will recognise digits in images uploaded (or drawn) by a user. The project uses [Flask](http://flask.pocoo.org/) and [TensorFlow](https://www.tensorflow.org/).

### Project Outline
1. Create a web application in Python to recognise digits in images.  

2. Users can visit the web application through their browser and submit or draw an image containing a single digit.  

3. The web application will respond with what it thinks the user's digit is.

### Getting Set Up
To clone this repository to your own machine, open the command line in the directory you wish to clone into and run `git clone https://github.com/rebeccabernie/EmergingTechProject.git`. Once the project has been cloned, type `cd EmergingTechProject` to open the project's directory.  

The project requires [Python 3](https://www.python.org/downloads/), [Flask](http://flask.pocoo.org/), and [TensorFlow](https://www.tensorflow.org/). If you haven't got Python 3 installed, I'd recommend using a distribution like 
[Anaconda](https://www.anaconda.com/download/) which simplifies installation and can be used to manage packages and updates. [Pillow](http://pillow.readthedocs.io/en/3.1.x/index.html) and [Numpy](http://www.numpy.org/) are used by the program to process and manipulate a given image into the right format for TensorFlow to perform operations on, so these libraries are also required. To install any of the above, run `pip3 install xyz` on the command line in the project folder, where xyz is the component to be installed - e.g. `pip3 install pillow`.  
*See full installation guides for each of the components for more detail: [Flask](http://flask.pocoo.org/docs/0.12/installation/), [TensorFlow](https://www.tensorflow.org/install/), [Pillow](http://pillow.readthedocs.io/en/3.1.x/installation.html), [Numpy](https://scipy.org/install.html).*  
*Note that the Numpy guide contains information for SciPy's other packages, which are not needed - only Numpy is required.*

#### Checkpoints
The training process for this neural network can take some time - in one case training on 3000 images, not even a quarter of the full training set, took over an hour. Standard machines may also freeze during the process. Even on a powerful machine the process would still take too long from a user's point of view, so I've included the model's checkpoints in the repository. The checkpoints folder contains the saved model training information so the network doesn't have to be trained on every run - if the folder is not present, run the `mnist.py` file - this will train the model on the MNIST training images. Once complete, `home.py` can be run as normal.

#### Accuracy
With current settings, the model is between 96-99% accurate. This is achieved using only 1,500 images of the available 20,000. If you'd like the best possible accuracy, increase the `range(1500)` on `line 80` of `mnist.py` and re-run the `mnist.py` file - this will retrain the model and save the new checkpoints. According to the TensorFlow [tutorial](https://www.tensorflow.org/get_started/mnist/pros), the highest accuracy this method gives is 99.2% by training all 20,000 images. Bear in mind that a high number will take much longer, and will also tend to make less of a difference to the end accuracy percentage - 1,500 has an accuracy of around 97%, 3,000 is about 98%, 10,000 may only be 98.5% and so on. At 1,500 images and , the project has yet to make a wrong prediction 


### User Guide
1. 

### Technologies


### Digit Recognition Feature
  * MNIST Data set, TensorFlow
  * One Hot Encoding: Data in format better suited to machine learning.  A *one hot vector* is a vector that has many dimensions, one containing a `1` and the rest containing `0`s. A `1` indicates that the vector is that category. In terms of MNIST, a digit `n` is represented as a `1` in the `n`th column. This data might look like: 

|     		| 0    | 1 	  | 2 	 | 3 	| 4    | 5 	  | 6 	 | 7 	| 8    | 9    |
|---- 		| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|Digit x    | 0    | 0 	  |0 	 | 1 	| 0    | 0 	  | 0 	 | 0 	| 0    | 0    |
|Digit y    | 0    | 0 	  |0 	 | 0 	| 0    | 0 	  | 0 	 | 1 	| 0    | 0    |
|Digit z    | 1    | 0 	  |0 	 | 0	| 0    | 0 	  | 0 	 | 0 	| 0    | 0    |

In this example, digit x is a 3, y is a 7 and z is a 0.

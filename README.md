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
To clone this repository to your own machine, open the command line in the directory you wish to clone into and run `git clone https://github.com/rebeccabernie/EmergingTechProject.git` - the checkpoints folder (explained below) is around 40mb in size so the repository may take a few minutes to download. Once the project has been cloned, type `cd EmergingTechProject` to open the project's directory. 

The project requires [Python 3](https://www.python.org/downloads/), [Flask](http://flask.pocoo.org/), and [TensorFlow](https://www.tensorflow.org/). If you haven't got Python 3 installed, I'd recommend using a distribution like 
[Anaconda](https://www.anaconda.com/download/) which simplifies installation and can be used to manage packages and updates. [Pillow](http://pillow.readthedocs.io/en/3.1.x/index.html) and [Numpy](http://www.numpy.org/) are used by the program to process and manipulate a given image into the right format for TensorFlow to perform operations on, so these libraries are also required. To install any of the above, run `pip3 install xyz` on the command line in the project folder, where xyz is the component to be installed - e.g. `pip3 install pillow`.  
*See full installation guides for each of the components for more detail: [Flask](http://flask.pocoo.org/docs/0.12/installation/), [TensorFlow](https://www.tensorflow.org/install/), [Pillow](http://pillow.readthedocs.io/en/3.1.x/installation.html), [Numpy](https://scipy.org/install.html).*  
*Note that the Numpy guide contains information for SciPy's other packages, which are not needed - only Numpy is required.*

#### Checkpoints
The training process for this neural network can take some time - in one case training on 3000 images, not even a quarter of the full training set, took over an hour. Standard machines may also freeze during the process. Even on a powerful machine the process would still take too long from a user's point of view, so I've included the model's checkpoints in the repository. The checkpoints folder contains the saved model training information so the network doesn't have to be trained on every run - if the folder is not present, run the `mnist.py` file - this will train the model on the MNIST training images. Once complete, `home.py` can be run as normal.

#### Accuracy
With current settings, the model is between 97-99% accurate. This is achieved using only 2,500 images of the available 20,000. If you'd like the best possible accuracy, increase the `range(1500)` on `line 80` of `mnist.py` and re-run the `mnist.py` file - this will retrain the model and save the new checkpoints. According to the TensorFlow [tutorial](https://www.tensorflow.org/get_started/mnist/pros), the highest accuracy this method gives is 99.2% by training all 20,000 images. Bear in mind that a high number will take much longer, and will also tend to make less of a difference to the end accuracy percentage - 1,500 has an accuracy of around 96%, 3,000 is about 98%, 10,000 may only be 98.5% and so on.

### User Guide
1. Once the project has been set up as described above, run `home.py` and open a browser window to http://127.0.0.1:5000/.
2. Use the `Choose File` button to select an image from your computer. I've included 500 sample MNIST test images in the [SampleImages](https://github.com/rebeccabernie/EmergingTechProject/tree/master/SampleImages) folder to choose from, which have not been used to train the model.
3. Click the `Upload File` button. The program's prediction will appear in the Prediction section.

![example](https://user-images.githubusercontent.com/14957616/33528679-448d4de0-d85c-11e7-9088-3a72239f209c.gif)


### Digit Recognition Feature
This project uses the training images contained in the [MNIST](http://yann.lecun.com/exdb/mnist/) database of handwritten digits to train a neural network to recognise patterns in images uploaded by the user. The network is trained on 2,500 images, retraining the network after each batch of 100 images.  
TensorFlow's `examples` module provides access to various example datasets, one of which is the MNIST set. The data is imported in the `mnist.py` file in one hot encoded format, a format better suited to machine learning.  A *one hot vector* is a vector that has many dimensions, one containing a `1` and the rest containing `0`s. A `1` indicates that the vector is that category. In terms of MNIST, a digit `n` is represented as a `1` in the `n`th column. This data might look like: 

|     		| 0    | 1 	  | 2 	 | 3 	| 4    | 5 	  | 6 	 | 7 	| 8    | 9    |
|---- 		| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|Digit x    | 0    | 0 	  |0 	 | 1 	| 0    | 0 	  | 0 	 | 0 	| 0    | 0    |
|Digit y    | 0    | 0 	  |0 	 | 0 	| 0    | 0 	  | 0 	 | 1 	| 0    | 0    |
|Digit z    | 1    | 0 	  |0 	 | 0	| 0    | 0 	  | 0 	 | 0 	| 0    | 0    |

In this example, digit x is a 3, y is a 7 and z is a 0.

Once the data is imported, the input, first convolutional, second convolutional, densely connected, and output layers are created. The model is then evaluated and trained. Once trained, the model can be tested against unseen MNIST data to give an accuracy reading. Finally, the program saves certain variables in the checkpoints file, which means the model only has to be trained once - after the first train, saved checkpoints are imported in the `runMnist.py` file and eliminate the need to train the model again.

### Known Problems
The neural network runs into issues when given particularly "messy" digits, such as the following two examples:  
![3](https://user-images.githubusercontent.com/14957616/33528686-5179608e-d85c-11e7-9b8e-bd59c79998a8.png) ![6](https://user-images.githubusercontent.com/14957616/33528698-8d6732ce-d85c-11e7-8956-e85ba044cd75.png)  
The first digit is classed as a 3, but is very similar to a skewed 8. The second is a 6, but looks similar to a 0.  
For most of the MNIST images, the predictions are accurate.  
I also came across an issue when testing with images drawn in Microsoft Paint. Images were 28x28 pixels in size and appear clear to the human eye, but the program was unable to predict digits correctly. See below:  
<img src="https://user-images.githubusercontent.com/14957616/33528746-6d398708-d85d-11e7-9e27-ac1181b7b335.JPG" height="300">  
Other than these issues, the program runs fine and predicts digits with almost 99% accuracy.


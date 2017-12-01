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

### Flask and Bootstrap

### Digit Recognition Feature
  * MNIST Data set, TensorFlow
  * One Hot Encoding: Data in format better suited to machine learning.  A *one hot vector* is a vector that has many dimensions, one containing a `1` and the rest containing `0`s. A `1` indicates that the vector is that category. In terms of MNIST, a digit `n` is represented as a `1` in the `n`th column. This data might look like: 

|     		| 0    | 1 	  | 2 	 | 3 	| 4    | 5 	  | 6 	 | 7 	| 8    | 9    |
|---- 		| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|Digit x    | 0    | 0 	  |0 	 | 1 	| 0    | 0 	  | 0 	 | 0 	| 0    | 0    |
|Digit y    | 0    | 0 	  |0 	 | 0 	| 0    | 0 	  | 0 	 | 1 	| 0    | 0    |
|Digit z    | 1    | 0 	  |0 	 | 0	| 0    | 0 	  | 0 	 | 0 	| 0    | 0    |

In this example, digit x is a 3, y is a 7 and z is a 0.

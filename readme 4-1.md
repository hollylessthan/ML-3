# Homework 4-1

**Introduction**
-
This code is written in Python 3.7.0 64-bit

**Explanation of the Code**
-
Based on the slides of Chapter 5, I implemented a backpropogation of error for the data provided. First of all, I used `rd.uniform` function to drive out initial weights for two hidden layers and one output layer. 

In the part A & B of the code, it was designed to calculate the value of hidden neurons using the sigmoid function.

In the part C of the code, it was designed to calculate the value of output neurons using the sigmoid function. 

In the part D of the code, it was designed for target vectors.

In the part E of the code, it was designed to calculate neuron’s responsibility for the output error.

In the part F of the code, it was designed to calculate the responsibilities of the hidden neurons by first calculating the weighted sums for each of the two hidden neurons.

In the part G of the code, it was designed to finally update the weights. After this process, backpropogation of error of one example had done.

This process wouldn't stop until all the example had go through.

In the end, I printed out the updated weights after one epoch had done.
(initial is the weight from x to hidden layer1, 
initial1 is the weight from hidden layer1 to hidden layer2,
initial2 is the weight from hidden layer2 to y)
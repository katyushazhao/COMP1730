## COMP1730/6730 Homework 2

# Your ANU ID: u7650690
# I declare that this submission is my own work
# [ref: https://www.anu.edu.au/students/academic-skills/academic-integrity ]
# Your NAME: Aria Zhao

import math

## You should implement the function `neural_network` below.
## You can use define new function(s) if it helps you decompose the problem
## into smaller problems.
def Sigma(x1, x2, w1, w2, b):
    return x1*w1 + x2*w2 + b

def ReLU(x):
    return max(0,x)

def sigmoid(x):
    return 1/(1+math.exp(-x))

def neural_network(x1, x2, x3, w1, w2, w3, w4, w5, w6, b1, b2, b3):
	return sigmoid(Sigma(ReLU(Sigma(x1,x2,w1,w2,b1)),ReLU(Sigma(x2,x3,w3,w4,b2)),w5,w6,b3))

################################################################################
#               DO NOT MODIFY ANYTHING BELOW THIS POINT
################################################################################    

def test_neural_network():
    '''
    This function runs a number of tests of the neural_network function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    NOTE: passing all tests does not automatically mean that your code is correct
    because this function only tests a limited number of test cases.
    '''

    assert math.fabs(neural_network(0, 0, 3.2, -0.1, 0.9, 0.7, -3.6, -1.0, -1.0, -1, -2.2, 0)  - 0.5) < 1e-6
    assert math.fabs(neural_network(0, 0, 3.2, -0.5, 1.9, 0.8, 1.0, 0.1, 1.3, -1, -2.2, 5.0)  - 0.9981670611) < 1e-6
    assert math.fabs(neural_network(0, 0, 3.2, -0.7, -0.4, -1.4, 4.1, -0.9, 2.6, 1, -2.2, 0)  - 1.0) < 1e-6
    assert math.fabs(neural_network(0, 0, 3.2, -0.9, 1.1, -0.7, -1.0, 0.7, -3.9, 1, -2.2, 5.0)  - 0.9966651927) < 1e-6
    assert math.fabs(neural_network(0, 2.5, 3.2, -0.9, 2.5, 0.0, -4.1, 1.0, 3.6, -1, -2.2, 0)  - 0.9947798743) < 1e-6
    assert math.fabs(neural_network(0, 2.5, 3.2, -0.8, -0.5, -1.5, -1.9, 0.2, -2.7, -1, -2.2, 5.0)  - 0.9933071491) < 1e-6
    assert math.fabs(neural_network(0, 2.5, 3.2, 0.4, -2.7, -1.3, 3.2, -0.2, -0.6, 1, -2.2, 0)  - 0.0534539038) < 1e-6
    assert math.fabs(neural_network(0, 2.5, 3.2, 0.2, -0.1, -0.5, -4.7, 0.5, 3.7, 1, -2.2, 5.0)  - 0.9953904278) < 1e-6
    assert math.fabs(neural_network(1, 0, 3.2, 1.0, 1.0, -0.6, -1.4, 0.4, 1.4, -1, -2.2, 0)  - 0.5) < 1e-6
    assert math.fabs(neural_network(1, 0, 3.2, -0.8, -1.6, -0.5, 0.1, 0.6, 0.0, -1, -2.2, 5.0)  - 0.9933071491) < 1e-6
    assert math.fabs(neural_network(1, 0, 3.2, -0.9, 1.9, -0.3, 0.2, -0.6, -0.6, 1, -2.2, 0)  - 0.4850044984) < 1e-6
    assert math.fabs(neural_network(1, 0, 3.2, -0.2, 1.6, -1.6, 0.5, -0.6, 1.6, 1, -2.2, 5.0)  - 0.98922827) < 1e-6
    assert math.fabs(neural_network(1, 2.5, 3.2, -0.9, -1.3, -0.6, 1.4, -0.9, -0.3, -1, -2.2, 0)  - 0.4417654819) < 1e-6
    assert math.fabs(neural_network(1, 2.5, 3.2, -0.6, -1.3, -0.1, 4.6, -0.0, 3.6, -1, -2.2, 5.0)  - 1.0) < 1e-6
    assert math.fabs(neural_network(1, 2.5, 3.2, -0.7, 2.5, -0.5, -3.1, 0.5, 3.3, 1, -2.2, 0)  - 0.9635611346) < 1e-6
    assert math.fabs(neural_network(1, 2.5, 3.2, -1.0, -1.4, 1.1, -1.6, -0.5, -3.9, 1, -2.2, 5.0)  - 0.9933071491) < 1e-6    

    print("all tests passed")

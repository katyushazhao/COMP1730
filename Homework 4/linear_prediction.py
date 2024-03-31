## COMP1730/6730 - Homework 4

# Your ANU ID: u7650690
# Your NAME: Aria Zhao
# I declare that this submission is my own work
# [ref: https://www.anu.edu.au/students/academic-skills/academic-integrity ]

## Implement the function below.
## (The statement "pass" is just a placeholder that does nothing: you
## should replace it.)
## You can define other functions if it helps you decompose the problem
## and write a better organised and/or more readable solution.

def linear_prediction(x, y, x_test):
    '''
    Returns the linear prediction at point x_test, sample given as two sequences x and y.
    It is assumed that y[i]=f(x[i]) and len(x)=len(y), all elements of x and y are assumed to be numbers.
    All elemets of x are assumed to be unique.
    Always returns a number.
    '''
    ordered = order(x,y)
    for (x,y) in ordered:
        if x == x_test:
            return y
    if ordered[0][0] < x_test < ordered[len(ordered)-1][0]:
        return interpolate(x_test, ordered)
    else:
        return extrapolate(x_test, ordered)

def order(x,y):
    '''
    order x in ascending order, order y relative to x so that y[i]=f(x[i]) still holds.
    x and y can be any sequence, returns ordered sequence as a tuple of tuples.
    It is assumed that y[i]=f(x[i]) and len(x)=len(y), all elements of x and y are assumed to be numbers.
    '''
    ordered = tuple(sorted(zip(x,y),key=lambda item: item[0]))
    return ordered

def extrapolate(x_test, ordered):
    '''
    Extrapolate f(x_test) given ordered tuple of tuples, Assumes x_test is outside the range of x.
    '''
    if x_test < ordered[0][0]:
        return pointgrad(ordered[0], ordered[1], x_test)
    else:
        return pointgrad(ordered[len(ordered)-2],ordered[len(ordered)-1],x_test)

def interpolate(x_test, ordered):
    '''
    Interpolate f(x_test) given ordered tuple of tuples, Assumes x_test is within the range of x.
    '''
    i = 0
    while ordered[i][0] < x_test:
        i += 1
    return pointgrad(ordered[i-1],ordered[i],x_test)

def pointgrad(near1, near2, x_test):
    '''
    Find equation of a straight line which passes through near1 and near2, assuming near1[x] < near2[x], return y on said line when x = x_test
    '''
    grad = (near2[1]-near1[1])/(near2[0]-near1[0])
    int = near1[1]-grad*near1[0]
    return grad*x_test + int

################################################################################
#               DO NOT MODIFY ANYTHING BELOW THIS POINT
################################################################################

def test_linear_prediction():
    '''
    This function runs a number of tests of the linear_prediction function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert abs(linear_prediction([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 0.5) - -1.0) < 1e-6
    assert abs(linear_prediction([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 2.0) - 5.0) < 1e-6
    assert abs(linear_prediction([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 4.0) - 17.0) < 1e-6
    assert abs(linear_prediction([1.0, 3.0, 5.0], (1.0, 9.0, 25.0), 6.0) - 33.0) < 1e-6
    assert abs(linear_prediction((1.0, 5.0, 3.0), [1.0, 25.0, 9.0], 1.25) - 2.0) < 1e-6
    assert abs(linear_prediction((1.0, 5.0, 3.0), (1.0, 25.0, 9.0), 2.5) - 7.0) < 1e-6

    # test that we get the right answer when x_test is exactly one
    # of the sample points:
    assert abs(linear_prediction([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 1) - 1.0) < 1e-6
    assert abs(linear_prediction([5.0, 1.0, 3.0], [25.0, 1.0, 9.0], 3) - 9.0) < 1e-6
    assert abs(linear_prediction([3.0, 1.0, 5.0], [9.0, 1.0, 25.0], 5) - 25.0) < 1e-6

    # we should get the same answer also if only the two adjacent
    # sample points are given:
    assert abs(linear_prediction([1.0, 3.0], [1.0, 9.0], 0) - -3) < 1e-6
    assert abs(linear_prediction([3.0, 1.0], [9.0, 1.0], 2.0) - 5.0) < 1e-6
    assert abs(linear_prediction([5.0, 3.0], [25.0, 9.0], 4.0) - 17.0) < 1e-6
    assert abs(linear_prediction([1.0, 3.0], [1.0, 9.0], 4.0) - 13.0) < 1e-6

    print("all tests passed")

import matplotlib.pyplot as plt

def plot_linear_prediction(x, y, x_tests):
    """
    This function visualizes linear_prediction results.
    It takes multiple x_test values as a sequence x_tests and
    data points specified in sequences x and y.
    Args:
        x: sequence of x-values
        y: sequence of corresponding y-values
        x_tests: sequence of testing x-values
    """
    y_tests = [ linear_prediction(x, y, x_test) for x_test in x_tests ]
    xlim_min = min(min(x), min(x_tests))-1
    ylim_min = min(min(y), min(y_tests))-3
    plt.xlim(xlim_min, max(max(x), max(x_tests))+1)
    plt.ylim(ylim_min, max(max(y), max(y_tests))+3)
    plt.plot(x, y, marker = "o", color = "black")
    for x_test, y_test in zip(x_tests, y_tests):
        plt.plot([xlim_min, x_test, x_test], [y_test, y_test, ylim_min], 
            linestyle = 'dashed')
    plt.show()

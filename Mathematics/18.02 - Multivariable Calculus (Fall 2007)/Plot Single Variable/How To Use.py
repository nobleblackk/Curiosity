# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:36:55 2019

@author: Yuvraj
"""
from SingleVarDifferntiation import SingleVarDifferntiation as sdiff
import numpy as np

# Step1: define a function example f(x) = 3x^2 + 4x + 5
def f(X):
    return 3*X**2 + 4*X + 5

# Step2: set a veriable as shown
d = sdiff(f, order_of_diff=1, x_range=(-10,10),dx=0.001) 
# Here the arguments are as follow
# Arg1: argument 1 is a function that you defined in Step1
# Arg2: argument 2 is the order of differentiation(it's isn't necesseary)
# Arg3: argument 3 is range of X-axis
# Arg4: argument 4 is dx difference in b/w 2 consecutive x values(the smaller the dx is the accurate the answer is, but slower will the runtime be)

# To plot the function
d.plot_function()

# To plot the nth derivative 
d.plot_derivative_order_n(1)
d.plot_derivative_order_n(2)

# to plot in new figure use argument plot_separately=True
d.plot_function(plot_separately=True)

# To plot Taylor Approximation at x near c, upto some number of terms of the Taylor series
# Use this method plot_Taylor_Approx()
# c is the value of x, no_of_taylor_terms is that some number of terms of the Taylor series
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 5)

# This the error term or remainder term that is the error in taylor approximation
# c is the value of x, no_of_taylor_terms is number of terms of the Taylor series
d.plot_error_term(c = 1, no_of_taylor_terms = 5)

# To set y limit in the plot Use method: set_ylimit()
# only 1 argumnet is received that is a tuple containing y range
d.set_ylimit((-15,15))

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 5)
d.plot_error_term(c = 1, no_of_taylor_terms = 5)


################################## Example 2 ##################################

# Well function specified in Step1 takes a numpy array as Input and gives corresponding numpy array as an output
# you don't have to specify any loop or anything else. numpy will handle it for you
# but if you use another functions like if you choose math.sqrt() rather than np.sqrt() then you have to use loop
# asshown bellow
def fun(x):
    import math
    output = []
    for i in range(len(x)):
        output.append(math.sqrt(x[i]))
    return np.array(output)
'''
d = sdiff(fun, x_range=(1,10),dx=0.01)
d.plot_function(plot_separately=True)
d.plot_derivative_order_n(1)
d.plot_derivative_order_n(2)

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 5)
d.plot_error_term(c = 1, no_of_taylor_terms = 5)
d.set_ylimit((-15,15))

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 5)
d.plot_error_term(c = 1, no_of_taylor_terms = 5)
#d.set_ylimit((-15,15))
'''

###############################################################################
############################# Example for sin(x) ##############################
    
def sin(x):
    return np.sin(x)

'''
d = sdiff(sin, order_of_diff=1, x_range=(-2*np.pi, 2*np.pi),dx=0.01) 
print("Critical points are x=",d.critical_points())
d.plot_function()
d.plot_derivative_order_n(1)
d.plot_derivative_order_n(2)

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(np.pi, 3)
d.plot_error_term(np.pi, 3)
d.set_ylimit((-1,1))

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(np.pi, 4)
d.plot_error_term(np.pi, 4)
d.set_ylimit((-1,1))

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(np.pi, 5)
d.plot_error_term(np.pi, 5)
d.set_ylimit((-1,1))
'''

###############################################################################
######################## Example for f(x) = 1/sqrt(x) #########################
    
def sqrt_inverse(X):
    return 1/np.sqrt(X)

'''
d = sdiff(sqrt_inverse, order_of_diff=1, x_range=(0,10),dx=0.1)
d.plot_function(plot_separately=True)
d.plot_derivative_order_n(1)
d.plot_derivative_order_n(2)

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 5)
d.plot_error_term(c = 1, no_of_taylor_terms = 5)
d.set_ylimit((-10,10))

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 8)
d.plot_error_term(c = 1, no_of_taylor_terms = 8)
d.set_ylimit((-10,10))
'''

###############################################################################
############################# Example for exp(x) ##############################
    
def exp(x):
    return np.exp(x)
'''
d = sdiff(exp, x_range=(-10,10),dx=0.01)
d.plot_function(plot_separately=True)
d.plot_derivative_order_n(1)
d.plot_derivative_order_n(2)

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 5)
d.plot_error_term(c = 1, no_of_taylor_terms = 5)
d.set_ylimit((-15,15))

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 5)
d.plot_error_term(c = 1, no_of_taylor_terms = 5)
d.set_ylimit((-15,15))
'''
###############################################################################
############################# Example for log(x) ##############################
    
def log(x):
    return np.log(x)

'''
d = sdiff(log, x_range=(-10,10),dx=0.01)
d.plot_function(plot_separately=True)
d.plot_derivative_order_n(1)
d.plot_derivative_order_n(2)
d.set_ylimit((-10,10))

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 5)
d.plot_error_term(c = 1, no_of_taylor_terms = 5)
d.set_ylimit((-10,10))

d.plot_function(plot_separately=True)
d.plot_Taylor_Approx(c = 1, no_of_taylor_terms = 5)
d.plot_error_term(c = 1, no_of_taylor_terms = 5)
d.set_ylimit((-10,10))
'''
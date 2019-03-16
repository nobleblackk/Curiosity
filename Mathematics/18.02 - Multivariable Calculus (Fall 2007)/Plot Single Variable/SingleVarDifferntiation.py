# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:49:36 2019

@author: Yuvraj
"""
import numpy as np
import matplotlib.pyplot as plt

class SingleVarDifferntiation:
    
    def __init__(self, function, order_of_diff = 1, x_range=(-10,10), dx = 0.1):
        SingleVarDifferntiation.__check_args__(function, order_of_diff, x_range, dx)
        self._function_ = function
        self._order_    = order_of_diff
        self._x_start_ = x_range[0]
        self._x_end_   = x_range[1]
        self.length    = 0
        self._dx_      = dx
        self._X_axis_  = None
        self._Y_axis_  = None
        self._ymin_    = 0
        self._ymax_    = 0
        self._Y_diff_  = None
        self._I_       = None
        self.__initialize__()

# =============================================================================        
        
    def __initialize__(self):
        counts = int((self._x_end_ - self._x_start_)/self._dx_) + 1
        self._X_axis_ = np.linspace(self._x_start_ , self._x_end_, counts)
        self._Y_axis_ = self._function_(self._X_axis_)
        min, max = SingleVarDifferntiation.__min_max__(self._Y_axis_)
        self.length = len(self._X_axis_)
        i = np.empty((1,self.length), dtype=float)
        i.fill(1.0)
        self._I_ = i[0]
        self._Y_diff_, min_max = self.__diff_order_n__(self._order_)
        self._ymin_,self._ymax_ = min, max
        

# =============================================================================        
        
    def __diff_wrt__(self, Y):
        Y2 = []
        dx = self._dx_
        min, max = None, None
        for i in range(self.length - 1):
            y2_y1 = Y[i+1] - Y[i]
            c = y2_y1/dx
            if(np.isfinite(c)):
                if(min == None or c < min):  min = c
                if(max == None or c > max):  max = c
            Y2.append(c)
        #x2 = self._X_axis_[-1] + dx
        #y2 = self._function_(x2)
        #y2_y1 = y2 - Y[-1]
        #Y2.append(y2_y1/dx)
        Y2.append(Y2[-1])
        return np.array(Y2), (min,max)

# =============================================================================        
    
    def __diff_order_n__(self,n):
        self._order_ = n
        Y = self._Y_axis_
        for i in range(n):
            Y, min_max = self.__diff_wrt__(Y)
        return  Y, min_max

# =============================================================================        
        
    def set_diff_order(self,n):
        self._order_ = n
        Y = self._Y_axis_
        for i in range(n):
            Y, min_max = self.__diff_wrt__(Y)
        self._Y_diff_ = Y
        #self._ymin_, self._ymax_ = min_max

# =============================================================================        
        
    def critical_points(self):
        l = []
        slope_is_positive = True
        if(self._Y_diff_[0] < 0): slope_is_positive = False
        for i in range(1,self.length):
            if(np.isfinite(self._Y_diff_[i])):
                if(self._Y_diff_[i] >= 0):                  # Slope is positive
                    if(slope_is_positive == False):         # It indicates that slope is negative previously
                        l.append(self._X_axis_[i])          # change of slope => critial point
                        slope_is_positive = True
                elif(self._Y_diff_[i] < 0):                 # Slope is negative
                    if(slope_is_positive == True):                # It indicates that slope is positive previously
                        l.append(self._X_axis_[i])          # change of slope => critial point
                        slope_is_positive = False
        return l

# =============================================================================        
    
    def factorial(self,n):
        res = 1
        for i in range(1,n+1):
            res *= i
        return res

# =============================================================================        
        
    # f(x)|x->c  = f{c} + (f'(c)/1!)*(x - c) + (f''(c)/2!)*(x - c)^2 + (f'''(c)/3!)*(x - c)^3 + (f''''(c)/4!)*(x - c)^4 + ...........
    
    def __taylorApprox__(self,c, no_of_taylor_terms = 3):
        if(c < self._x_start_ or c > self._x_end_):
            raise ValueError("c must be in range of x-axis: (" + str((self._x_start_,self._x_end_)) + ')')
        index = round((c - self._x_start_) / self._dx_)
        approx = self._I_ * self._Y_axis_[index]
        Y = self._Y_axis_
        X = self._X_axis_ - c
        for i in range(no_of_taylor_terms):
            Y, min_max = self.__diff_wrt__(Y)
            approx = approx + (Y[index]/self.factorial(i))*X
            X = X*(self._X_axis_ - c)
        return approx, min_max
    
    def __error_term__(self,c, no_of_taylor_terms = 3):
        taylor_approx, min_max = self.__taylorApprox__(c, no_of_taylor_terms)
        error = self._Y_axis_ - taylor_approx
        return error, min_max

# =============================================================================        
    
    def plot_Taylor_Approx(self, c, no_of_taylor_terms = 3, plot_separately = False):
        if(plot_separately): plt.figure()
        Y, min_max = self.__taylorApprox__(c,no_of_taylor_terms)
        lab = 'Taylor Approx (' + str(no_of_taylor_terms) + ')'
        index = round((c - self._x_start_) / self._dx_)
        x,y = self._X_axis_[index], self._Y_axis_[index]
        plt.scatter(x,y)
        self.__plot__(self._X_axis_, Y, lab, min_max)

# =============================================================================        
    
    def plot_error_term(self, c, no_of_taylor_terms = 3, plot_separately = False):
        if(plot_separately): plt.figure()
        Y, min_max = self.__error_term__(c,no_of_taylor_terms)
        lab = 'Error Term (' + str(no_of_taylor_terms) + ')'
        index = round((c - self._x_start_) / self._dx_)
        x,y = self._X_axis_[index], self._Y_axis_[index]
        plt.scatter(x,y)
        self.__plot__(self._X_axis_, Y, lab, min_max)

# =============================================================================        
    
    def plot_function(self, plot_separately = False):
        if(plot_separately): plt.figure()
        self.__plot__(self._X_axis_, self._Y_axis_, 'y = f(x)', (self._ymin_, self._ymax_))

# =============================================================================        
        
    def plot_derivative(self, plot_separately = False):
        if(plot_separately): plt.figure()
        lab = 'Diff order ' + '(' + str(self._order_) + ')'
        self.__plot__(self._X_axis_, self._Y_diff_, lab, (self._ymin_, self._ymax_))
        
    def plot_derivative_order_n(self, n, plot_separately = False):
        if(n == self._order_): self.plot_derivative(plot_separately)
        else:
            if(plot_separately): plt.figure()
            lab = 'Diff order ' + '(' + str(n) + ')'
            Y, min_max = self.__diff_order_n__(n)
            self.__plot__(self._X_axis_, Y, lab, min_max)

# =============================================================================        
        
    def __plot__(self,X,Y,_label,yrange):
        plt.title(self._function_.__name__)
        plt.plot(X, Y, label = _label)
        plt.legend()
        plt.show()

    def set_ylimit(self,limit_range):
        if(type(limit_range) != tuple and len(limit_range) != 2):
            raise ValueError("limit_range must be ot type tuple with length 2")
        ymin,ymax = limit_range[0], limit_range[1]
        axes = plt.gca()
        axes.set_ylim([ymin,ymax])
        
# =============================================================================        
        
    @staticmethod
    def __check_args__(function, order_of_diff, x_range, dx):
        if(function.__class__.__name__ != 'function'):
            raise TypeError("argument1 must be a function that take x as input and return y as output")
        if(type(order_of_diff) != int):
            raise TypeError("order_of_diff must be of type 'int'")
        if(order_of_diff < 1):
            raise ValueError("order_of_diff must be greater then 1")
        if(type(x_range) != tuple):
            raise TypeError("x_range must be of type tuple")
        if(len(x_range) != 2):
            raise ValueError("x_range must contain a range for X-axis a start and a end")
        if(x_range[0] > x_range[1]):
            raise ValueError("start must be less the end")
        if(type(order_of_diff) != float and type(order_of_diff) != int):
            raise TypeError("order_of_diff must be of type 'float' or 'int'")
        if(dx <= 0):
            raise ValueError("dx must not be >0")

    @staticmethod
    def __min_max__(l):
        min, max = None, None
        for c in l:
            if(np.isfinite(c)):
                if(min == None or c < min):
                    min = c
                if(max == None or c > max):
                    max = c
        return min,max
            
''' ===========================================================================        
    ==============================  In Progress  ==============================
    ===========================================================================
'''
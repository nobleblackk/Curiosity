# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 04:50:55 2019

@author: Yuvraj
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MultiVariable:
    
    def __init__(self,function, x_range, dx, y_range, dy):
        self._function_ = function
        self._x_start_ = x_range[0]
        self._x_end_   = x_range[1]
        self._y_start_ = y_range[0]
        self._y_end_   = y_range[1]
        self._dx_      = dx
        self._dy_      = dy
        self._X_axis_1D  = None
        self._Y_axis_1D  = None
        self._X_axis_  = None
        self._Y_axis_  = None
        self._Z_axis_  = None
        self._Zero_    = None
        self._Y_len_   = None
        self._X_len_   = None
        self.__initialize__()

# =============================================================================        

    def __initialize__(self):
        counts = int((self._x_end_ - self._x_start_)/self._dx_) + 1
        X = np.linspace(self._x_start_ , self._x_end_, counts)
        counts = int((self._y_end_ - self._y_start_)/self._dy_) + 1
        Y = np.linspace(self._y_start_ , self._y_end_, counts)
        self._X_len_ = len(X)
        self._Y_len_ = len(Y)
        self._X_axis_1D = X.copy()
        self._Y_axis_1D = Y.copy()
        X, Y = np.meshgrid(X,Y)
        Z = np.empty(X.shape)
        self._X_axis_, self._Y_axis_ = X, Y
        for i in range(len(X)):
            for j in range(len(X[i])):
                Z[i][j] = self._function_(X[i][j],Y[i][j])
        self._Z_axis_ = Z
        shape = Z.shape
        Zero = np.empty(shape)
        Zero.fill(0.0)
        self._Zero_ = Zero

# =============================================================================        
    
    def plot_surface_color_3D(self, plot_separately = True):
        if(plot_separately): plt.figure()
        self.__plot_3D_curve__(self._X_axis_, self._Y_axis_, self._Z_axis_, self._function_.__name__)

    def __plot_3D_curve__(self, X, Y, Z, title,diff_order=(0,0)):
        ax = plt.gca(projection='3d')
        remove_x,remove_y = diff_order
        if(remove_x != 0):
            Z = Z[:,:-remove_x]
            X = X[:,:-remove_x]
            Y = Y[:,:-remove_x]
            
        if(remove_y != 0):
            Z = Z[:-remove_y,:]
            Y = Y[:-remove_y,:]
            X = X[:-remove_y,:]
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
        self.__plot_3D__(ax,title)


# =============================================================================        

    def __plot_3D__(self,ax,title):
        plt.title(title)#self._function_.__name__
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        ax.legend()
        plt.show()

# =============================================================================        
        
    def plot_surface_lines_3d(self, plot_separately = True):
        if(plot_separately): fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.contour3D(self._X_axis_, self._Y_axis_, self._Z_axis_, 50, cmap='binary')
        self.__plot_3D__(ax,self._function_.__name__)

# =============================================================================        

    def __get_Z_wrtX__(self,x_value):
        Z = []
        for y in self._Y_axis_1D:
            Z.append(self._function_(x_value,y))
        return Z

# =============================================================================        
    
    def __get_Z_wrtY__(self,y_value):
        Z = []
        for x in self._X_axis_1D:
            Z.append(self._function_(x,y_value))
        return Z

# =============================================================================        

    def __diff__(self,X, Y):
        Y2 = []
        dx = X[1] - X[0]
        for i in range(len(Y) - 1):
            y2_y1 = Y[i+1] - Y[i]
            c = y2_y1/dx
            Y2.append(c)
        Y2.append(Y2[-1])
        return np.array(Y2)

# =============================================================================        

    def __diff_wrtX_given_Y_order_n__(self, n, y_value):
        Z = self.__get_Z_wrtY__(y_value)
        for i in range(n):
            Z = self.__diff__(self._X_axis_1D, Z)
        return Z

# =============================================================================        

    def __diff_wrtY_given_X_order_n__(self, n, x_value):
        Z = self.__get_Z_wrtX__(x_value)
        for i in range(n):
            Z = self.__diff__(self._Y_axis_1D, Z)
        return Z

# =============================================================================        


    def __plot_function_wrt__(self, axis, value, wrt, Z, _label, diff_order = 0, plot_separately = True):
        if(plot_separately):
            fig = plt.figure()
            ax = fig.gca(projection='3d')
        else: ax = plt.gca(projection='3d')
        if(diff_order !=0):
            axis = axis[:-diff_order]
            Z = Z[:-diff_order]
        ax.plot(axis, Z, zs=value, zdir=wrt, label= _label)
        title = 'd('+self._function_.__name__+")/d("+wrt+")"
        self.__plot_3D__(ax,title)

# =============================================================================        
    
    def plot_function_wrtX(self,x_value, plot_2D_or_3D = '3D', plot_separately = True):
        Z = self.__get_Z_wrtX__(x_value)
        label = 'f(x,y)|x='+str(x_value)
        if(plot_2D_or_3D.lower() == '2d'):
            self.__plot_2D__(self._Y_axis_1D, Z, label, plot_separately)
        elif(plot_2D_or_3D.lower() == '3d'):
            self.__plot_function_wrt__(self._Y_axis_1D, x_value, 'x', Z, label, plot_separately)
        else: raise ValueError("'plot_2D_or_3D' must be either '2D' or '3D'")   

# =============================================================================        
        
    def plot_function_wrtY(self, y_value, plot_2D_or_3D = '3D', plot_separately = True):
        Z = self.__get_Z_wrtY__(y_value)
        label = 'f(x,y)|y='+str(y_value)
        if(plot_2D_or_3D.lower() == '2d'):
            self.__plot_2D__(self._X_axis_1D, Z, label, plot_separately)
        elif(plot_2D_or_3D.lower() == '3d'):
            self.__plot_function_wrt__(self._X_axis_1D, y_value, 'y', Z, label, plot_separately)
        else: raise ValueError("'plot_2D_or_3D' must be either '2D' or '3D'")   

# =============================================================================        

    def __diff_wrtX__(self, order_of_diff = 1):
        Z2 = []
        for y_value in self._Y_axis_1D:
            Z2.append(self.__diff_wrtX_given_Y_order_n__(order_of_diff, y_value))
        return np.array(Z2)
    
    def plot_diff_wrtX(self,order_of_diff = 1, plot_separately = True):
        if(plot_separately): plt.figure()
        Z = self.__diff_wrtX__(order_of_diff)
        #l = "".join(['x' for _ in range(order_of_diff)])
        #title1 = self._function_.__name__+'_'+l
        #l = "".join(['d('+_+')' for _ in l])
        title2 = 'd'+str(order_of_diff)+'('+self._function_.__name__+')/d'+str(order_of_diff)+'(x)'
        self.__plot_3D_curve__(self._X_axis_, self._Y_axis_, Z,title2, diff_order=(order_of_diff, 0))
        
    def __diff_wrtY__(self, order_of_diff = 1):
        Z2 = []
        for x_value in self._X_axis_1D:
            Z2.append(self.__diff_wrtY_given_X_order_n__(order_of_diff, x_value))
        return np.array(Z2).T
    
    def plot_diff_wrtY(self, order_of_diff = 1, plot_separately = True):
        if(plot_separately): plt.figure()
        Z = self.__diff_wrtY__(order_of_diff)
        title = 'd'+str(order_of_diff)+'('+self._function_.__name__+')/d'+str(order_of_diff)+'(y)'
        self.__plot_3D_curve__(self._X_axis_, self._Y_axis_, Z, title, diff_order=(0, order_of_diff))

# =============================================================================

    def __get_Z_wrtY_given_Z__(self, y_value, Z):
        index = int(round((y_value - self._Y_axis_1D[0]) / self._dy_))
        return Z[index]

    def __get_Z_wrtX_given_Z__(self, x_value, Z):
        index = int(round((x_value - self._X_axis_1D[0]) / self._dx_))
        Z2 = []
        for i in range(len(Z)):
            Z2.append(Z[i][index])
        return np.array(Z2)

    def __diff_wrtX_given_Z__(self, Z):
        Z2 = []
        for y_value in self._Y_axis_1D:
            z = self.__get_Z_wrtY_given_Z__(y_value, Z)
            z = self.__diff__(self._X_axis_1D, z)
            Z2.append(z)
        return np.array(Z2)
    
    def __diff_wrtY_given_Z__(self, Z):
        Z2 = []
        for x_value in self._X_axis_1D:
            z = self.__get_Z_wrtX_given_Z__(x_value, Z)
            z = self.__diff__(self._Y_axis_1D, z)
            Z2.append(z)
        return np.array(Z2).T
    
    def __diff_of_seq__(self,seq):
        if(type(seq) != str): raise TypeError("type of sequence must be 'str'")
        for x in seq:
            if(x.lower() != 'x' and x.lower() != 'y'): raise ValueError("sequence must contain either 'x' or 'y'")
        Z = self._Z_axis_.copy()
        for c in seq:
            if(c == 'x'):
                Z = self.__diff_wrtX_given_Z__(Z)
            else:
                Z = self.__diff_wrtY_given_Z__(Z)
        return Z
    
    def plot_diff_of_sequence(self, sequence, plot_separately = True):
        if(plot_separately): plt.figure()
        Z = self.__diff_of_seq__(sequence)
        #title = self._function_.__name__+'_'+sequence
        #l = "".join(['d('+_+')' for _ in sequence])
        xs,ys = 0,0
        for s in sequence:
            if(s =='x'): xs += 1
            else: ys += 1
        title = 'd'+str(len(sequence))+'('+self._function_.__name__+')/'+'d'+str(xs)+'(x)d'+str(ys)+'(y)'
        self.__plot_3D_curve__(self._X_axis_, self._Y_axis_, Z, title, diff_order=(xs,ys))
        
# =============================================================================        

    def plot_diff_wrtY_given_X(self, x_value, order_of_diff = 1, plot_2D_or_3D = '3D', plot_separately = True):
        Z = self.__diff_wrtY_given_X_order_n__(order_of_diff, x_value)
        label = "Diff(" + str(order_of_diff) + ')|x=' + str(x_value)
        if(plot_2D_or_3D.lower() == '2d'):
            self.__plot_2D__(self._Y_axis_1D, Z, label, order_of_diff, plot_separately)
        elif(plot_2D_or_3D.lower() == '3d'):
            self.__plot_function_wrt__(self._Y_axis_1D, x_value, 'x', Z, label, order_of_diff, plot_separately)
        else: raise ValueError("'plot_2D_or_3D' must be either '2D' or '3D'")

# =============================================================================        

    def plot_diff_wrtX_given_Y(self, y_value, order_of_diff = 1, plot_2D_or_3D = '3D', plot_separately = True):
        Z = self.__diff_wrtX_given_Y_order_n__(order_of_diff, y_value)
        label = "Diff(" + str(order_of_diff) + ')|y=' + str(y_value)
        if(plot_2D_or_3D.lower() == '2d'):
            self.__plot_2D__(self._X_axis_1D , Z, label, order_of_diff, plot_separately)
        elif(plot_2D_or_3D.lower() == '3d'):
            self.__plot_function_wrt__(self._X_axis_1D, y_value, 'y', Z, label, order_of_diff, plot_separately)
        else: raise ValueError("'plot_2D_or_3D' must be either '2D' or '3D'")    

# =============================================================================        

    def __plot_2D__(self, X, Y, _label, order_of_diff=0, plot_separately = True):
        if(plot_separately):
            plt.figure()
            plt.title(self._function_.__name__)
        else:
            ax = plt.gca()
            try:
                ax.get_zlim() # => if current figure is of 3D
                plt.figure()  # So Create new fig
                plt.title(self._function_.__name__)
            except:
                pass
        if(order_of_diff != 0):
            X = X[:-order_of_diff]
            Y = Y[:-order_of_diff]
        plt.plot(X, Y, label= _label)
        plt.legend()
        plt.show()

# =============================================================================        
        
    def setZ_limit(self,limit_range):
        if(type(limit_range) != tuple): raise ValueError("limit_range must be of type 'tuple'")
        ax = plt.gca(projection='3d')
        ax.set_zlim(limit_range[0], limit_range[1])

    def setY_limit(self,limit_range):
        if(type(limit_range) != tuple): raise ValueError("limit_range must be of type 'tuple'")
        ax = plt.gca(projection='3d')
        ax.set_ylim(limit_range[0], limit_range[1])

    def setX_limit(self,limit_range):
        if(type(limit_range) != tuple): raise ValueError("limit_range must be of type 'tuple'")
        ax = plt.gca(projection='3d')
        ax.set_xlim(limit_range[0], limit_range[1])

    def set_axes_limit(self, limit):
        if(type(limit) != tuple): raise ValueError("limit must be of type 'tuple'")
        self.setX_limit(limit)
        self.setY_limit(limit)
        self.setZ_limit(limit)

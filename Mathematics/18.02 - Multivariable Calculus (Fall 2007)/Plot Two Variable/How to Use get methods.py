# -*- coding: utf-8 -*-
"""
Created on Fri May 17 04:50:42 2019

@author: Yuvraj Garg
"""

import MultiVariable as mvar

def f(X,Y):
    return X**4 + Y**4 + (X**2)*Y + Y*(X**3) + X*Y

x_axis, y_axis,  dx, dy = (-10,10) ,(-10,10) ,0.5 ,0.5
m = mvar.MultiVariable(f, x_axis, dx, y_axis, dy)


'''   =================   How to use get's methods   =================  '''

# Now suppose you wanna take slice of some derivative of function
# For example we take derivative: df/dx
# 1st get Z-axis(or say function) of that derivative
Z = m.getZ_diff_wrtX(order_of_diff = 1)

# Now say you wanna take slice of df/dx at x = 1
# we use method 'plot_function_wrtX' and send derivative 'Z'
# important argument here is 'Z'
m.plot_function_wrtX(x_value=1, plot_2D_or_3D='2D', plot_separately=True, Z = Z)

# Now to take take slice of df/dx at y = 1
m.plot_function_wrtY(y_value=1, plot_2D_or_3D='2D', plot_separately=True, Z = Z)

# To plot df/dx you can use plot_surface_color_3D method
m.plot_surface_color_3D(Z=Z)

# You can do it for different derivative like D_xx, D_xy, D_xyxy, ......
# Example for D_xx
# 1st get Z-axis(or say function) of that derivative D_xx
sequence_of_diff = 'xx'
Z = m.getZ_diff_of_sequence(sequence_of_diff)
# Plot D_xx
m.plot_surface_color_3D(Z=Z)
# To take slice of D_xx at x = 1
m.plot_function_wrtX(x_value=1, plot_2D_or_3D='2D', plot_separately=True, Z = Z)
# To take take slice of D_xx at y = 1
m.plot_function_wrtY(y_value=1, plot_2D_or_3D='2D', plot_separately=True, Z = Z)

''' You will get some error at end of plot you can get rid by that by just specifing order of differentiation '''
# Lets redo previous example
# 1st get Z-axis(or say function) of that derivative D_xx
sequence_of_diff = 'xx'
Z = m.getZ_diff_of_sequence(sequence_of_diff)
# now while plotting just specify sequence of differentiation by variable 'sequence_of_diff'
m.plot_surface_color_3D(Z=Z,sequence_of_diff=sequence_of_diff)
# To take slice of D_xx at x = 1
m.plot_function_wrtX(x_value=1, plot_2D_or_3D='2D', plot_separately=True, Z = Z,sequence_of_diff=sequence_of_diff)
# To take take slice of D_xx at y = 1
m.plot_function_wrtY(y_value=1, plot_2D_or_3D='2D', plot_separately=True, Z = Z,sequence_of_diff=sequence_of_diff)

# plotting d(D_xx)/dx
m.plot_diff_wrtX(Z=Z,sequence_of_diff=sequence_of_diff)  # it's equivalent to plot D_xxx
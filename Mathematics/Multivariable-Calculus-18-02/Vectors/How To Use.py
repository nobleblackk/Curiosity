# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:51:49 2019

@author: Yuvraj
"""

from Vector import Vector,Plane

'''
###############################################################
################### How to use Vector class ###################
###############################################################    
'''

''' These are the basis vectors '''
i = Vector([1,0,0]) # 1i + 0j + 0k
j = Vector([0,1,0]) # 0i + 1j + 0k
k = Vector([0,0,1]) # 0i + 0j + 1k

v1 = Vector([  8,  48,  33]) #   8i +48j +33k 
v2 = Vector([ -6,  80,  86]) #  -6i +80j +86k 
v3 = Vector([-51,  25,  74]) # -51i +25j +74k
v4 = Vector([ 43, -42, -30]) #  43i -42j -30k
v5 = Vector([-69, -69, -40]) # -69i -69j -40k

''' To get the magnitude of a vector '''
magnitude_v1 = v1.magnitude()
magnitude_v2 = v2.magnitude()

''' To get the x,y,z coordinatesof a vector '''
x, y, z = v1[0],v1[1],v1[2]

''' To add to vectors '''
v = v1 + v2

''' To subtract two vectors '''
v = v1 - v2

''' To take the cross-product of two vectors '''
v = v1 * v2
    # OR
v = v1.cross(v2)

''' To take the dot-product of two vectors '''
v = v1.dot(v2)

''' To compare magnitude of to vectors '''
t = v1 > v2
t = v1 < v2
t = v1 >= v2
t = v1 <= v2

''' To check if two vectors are equall or not '''
t = v1 == v2
t = v1 != v2

''' To scale a vector '''
v = v1 * 2
v = v1 / 2
   # OR
v = v1.scale(2)
v = v1.scale(1/2)

''' Negate of a vector '''
v = -v1

''' To copy a vector '''
v = v1.copy()

''' To get a unit-vector '''
v = v1.unit_vector()

'''  Angle b/w 2 vectors '''
angle = v1.angle(v2)

''' To check if two vectors are parallel '''
is_parallel = v1.is_parallel_to_vector(v2)

''' To check if two vectors are perpendicular '''
is_perpendicular = v1.is_perpendicular_to_vector(v2)

''' To get the volume of a parallelopiped '''
volume = Vector.volume(v1,v2,v3)

''' To get area b/w 2 vectors '''
area = Vector.area(v1,v2)

''' To check if a vector is parallel to a plane '''
# is_parallel = v1.is_parallel_to_plane(plane) # Here plane is object of class Plane

''' To check if a vector is is_perpendicular to a plane '''
# is_perpendicular = v1.is_perpendicular_to_plane(plane) # Here plane is object of class Plane

'''
###########################################################
################ How to use Plane class ###################
###########################################################
'''

''' Create a Plane object specifing normal_vector, constant '''
normal_vector, constant = Vector([-2,-3, 3]), 5
plane = Plane([normal_vector,constant]) # -2x -3y +3z +5 = 0

''' Create a Plane object passing through 3 points in space '''
''' Specify 3 points in 3-D space '''
p1, p2, p3 = (1, 1, 0), (1, 2, 1), (-2, 2, -1)
''' To get the Plane passing through 3 points in space '''
plane = Plane([p1,p2,p3])   # -2x -3y +3z +5 = 0
    # OR
plane = Plane.get_plane_passing_through_3_points(p1,p2,p3)

''' To get normal vector and constant of a Plane object '''
normal_vector, constant = plane.get_normal_vector_and_constant()

''' Create a Plane object specifing normal vector and a point on a plane '''
plane = Plane([normal_vector,p1])  # -2x -3y +3z +5 = 0
      #  OR
plane = Plane.get_plane_given_normal_vector_and_a_point(normal_vector,p1)

# Creating 2 planes
p1, p2, p3 = (0,0,0), (4, 0, -2), (0, 8, -6)
plane1 = Plane([p1,p2,p3])                      # 16x +24y +32z +0 = 0

p1, p2, p3 = (1, -2, 0), (3, 1, 4), (0, -1, 2)
plane2 = Plane([p1,p2,p3])                      # 2x -8y +5z -18 = 0

''' To add two planes p1 + p2 '''
plane = plane1 + plane2

''' To subtract two planes p1 - p2 '''
plane = plane1 - plane2

''' To scale a planes(it scales normal vectow along with the constant) '''
plane = plane1 * 2
plane = plane1 / 2
    # OR
plane = plane1.scale(2)
plane = plane1.scale(1/2)

''' To check is two planes are parallel '''
is_parallel = plane1.is_parallel_to_plane(plane1)
is_parallel = plane1.is_parallel_to_plane(plane2)

''' To check is two planes are perpendicular '''
is_perpendicular = plane1.is_perpendicular_to_plane(plane1)
is_perpendicular = plane1.is_perpendicular_to_plane(plane2)

''' To check if a planes and a vector are parallel '''
is_parallel = plane1.is_parallel_to_vector(v1)

''' To check if a planes and a vector are perpendicular '''
is_perpendicular = plane1.is_perpendicular_to_vector(v1)

''' To get angle b/w 2 planes '''
angle = plane1.angle(plane2)
angle = plane1.angle(plane1)


''' plane passing through intersection of two planes and passing through a point '''
''' plane1 =  x +  y +  z - 6 = 0 ;  plane1 : normal_vector = <1,1,1> , constant = -6 '''
''' plane2 = 2x + 3y + 4z - 5 = 0 ;  plane1 : normal_vector = <2,3,4> , constant = -5 '''
normal_vector1, constant1 = Vector([1,1,1]), -6
normal_vector2, constant2 = Vector([2,3,4]),  5
plane1 = Plane([normal_vector1, constant1])  #  x +  y +  z - 6 = 0
plane2 = Plane([normal_vector2, constant2])  # 2x + 3y + 4z - 5 = 0
point  = (1,1,1)
plane3 = Plane.get_plane_through_intersection_of_planes_and_a_point(plane1,plane2,point)

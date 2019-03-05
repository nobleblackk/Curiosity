# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 06:23:28 2019

@author: Yuvraj
"""
from numpy import arccos,pi,warnings
from math import sqrt

class Plane:
    def __init__(self,arguments):
        self.normal_vector = None
        self.constant = None
        """
            Arguments: arguments is a list of items. Items can be:
                1. A list of [3 points on the plane]
                2. A list of [Normal Vector and a point on a plane]
                3. A list of [Normal Vector and a constant]
                4. A list containing [a, b, c, d] for plane of type: ax + by + cz + d = 0

            Here Plane is of form: ax + by + cz + d = 0
            where the vector <a, b, c> is the self.normal vector (normal to the plane) and d is self.constant
        """
        if(type(arguments) != list and type(arguments) != tuple):
            raise TypeError("Argument must be a list or tuple you have provided argument of type: "+ str(arguments.__class__.__name__))
        elif(len(arguments) != 2 and len(arguments) !=3 and len(arguments) !=4):
            #print(arguments)
            raise ValueError(""" Invalid argument arg must be a list of items. Items can be:
                1. A list/tuple of [3 points on the plane]
                2. A list/tuple of [Normal Vector and a point on a plane]
                3. A list of [Normal Vector and a constant]
                4. A list containing [a, b, c, d] for plane of type: ax + by + cz + d = 0""")
        elif(len(arguments) == 2):
            Plane.__checkForVector__(arguments[0])
            if(type(arguments[1]) == list or type(arguments[1]) == tuple):
                Plane.__checkForPoint__(arguments[1])
                self.__get_plane_given_normal_vector_and_a_point__(arguments[0],arguments[1])
            elif(type(arguments[1]) == int or type(arguments[1]) == float):
                self.normal_vector = arguments[0]
                self.constant = arguments[1]
                
        elif(len(arguments) == 3):
            Plane.__checkForPoint__(arguments[0])
            Plane.__checkForPoint__(arguments[1])
            Plane.__checkForPoint__(arguments[2])
            self.__get_plane_passing_through_3_points__(arguments[0],arguments[1],arguments[2])
        elif(len(arguments) == 4):
            Plane.__checkForPlaneElements__(arguments)
            self.normal_vector = Vector([arguments[0],arguments[1],arguments[2]])
            self.constant      = arguments[3]

    @staticmethod
    def __checkForVector__(vector):
        Vector.__check_if_arg_is_vector__(vector)
        
    @staticmethod
    def __checkForPoint__(point):
        Plane.__checkForPlaneElements__(point)
        if(len(point) != 3):
            raise ValueError("Points must be 3 Dimentional not " + str(len(point)) + " Dimentional ")
    
    @staticmethod
    def __checkForPlane__(plane):
        if(plane.__class__.__name__ != Plane.__name__):
            raise TypeError("Argument must be of type: " + str(Plane.__name__) + ' you have passed: '  +str(plane.__class.__name))
            
    @staticmethod
    def __checkForPlaneElements__(arguments):
        is_int, is_float = True, True
        for i in range(len(arguments)):
            if(type(arguments[i]) != int):  is_int = False
        for i in range(len(arguments)):
            if(type(arguments[i]) != float):    is_float = False
        if(not is_float and not is_int):
            if(len(arguments)==1): raise TypeError("Argument must be of type: int/float you have provided argument of type: "+ str(arguments[0].__class__.__name__))
            else: raise TypeError("Every element must be of type: int/float")
        
    def __str__(self):
        return self.__planeString__()
    
    def __repr__(self):
        return self.__planeString__()
        
    def __add__(self, plane):
        Plane.__checkForPlane__(plane)
        v = self.normal_vector + plane.normal_vector 
        constant = self.constant + plane.constant
        v._vector_.append(constant)
        return Plane(v._vector_)
    
    def __eq__(self, plane):
        Plane.__checkForPlane__(plane)
        if(self.normal_vector == plane.normal_vector and self.constant == plane.constant):
            return True
        return False
    
    def __sub__(self, plane):
        Plane.__checkForPlane__(plane)
        v = self.normal_vector - plane.normal_vector 
        constant = self.constant - plane.constant
        v._vector_.append(constant)
        return Plane(v._vector_)
    
    def __mul__(self,scalingFactor):
        Plane.__checkForPlaneElements__([scalingFactor])
        return self.scale(scalingFactor)
    
    def __truediv__(self,scalingFactor):
        Plane.__checkForPlaneElements__([scalingFactor])
        return self.scale(1/scalingFactor)
    
    def scale(self,scalingFactor):
        v = self.normal_vector * scalingFactor
        constant = self.constant * scalingFactor
        v._vector_.append(constant)
        return Plane(v._vector_)
    
        
    def __planeString__(self):
        normal_vector, constant = self.normal_vector, self.constant
        x, y, z = normal_vector[0], normal_vector[1], normal_vector[2] # These are the coefficients of x, y, z respectively
        s = str(x) + 'x' 
        if(y>=0): s = s + ' +' +str(y) +'y'
        else:     s = s + ' ' +str(y) +'y'
        if(z>=0): s = s + ' +' +str(z) +'z'
        else:     s = s + ' ' +str(z) +'z'
        if(constant>=0): s = s + ' +' +str(constant)
        else:     s = s + ' ' +str(constant)
        return s + ' = 0'

    def is_parallel_to_plane(self,plane):
        Plane.__checkForPlane__(plane)
        angle = self.angle(plane)
        if(angle == 0): return True
        return False
    
    def is_perpendicular_to_plane(self,plane):
        Plane.__checkForPlane__(plane)
        angle = self.angle(plane)
        if(angle == pi/2): return True
        return False
    
    def is_parallel_to_vector(self,vector):
        Plane.__checkForVector__(vector)
        angle = self.normal_vector.angle(vector)
        if(angle == pi/2): return True
        return False
    
    def is_perpendicular_to_vector(self,vector):
        Plane.__checkForVector__(vector)
        angle = self.normal_vector.angle(vector)
        if(angle == 0): return True
        return False
    
    
    def angle(self,plane):
        Plane.__checkForPlane__(plane)
        return self.normal_vector.angle(plane.normal_vector)
    
    def get_normal_vector_and_constant(self):
        return self.normal_vector, self.constant
    
    @staticmethod
    def get_plane_passing_through_3_points(point1, point2, point3):
        Plane.__checkForPoint__(point1)
        Plane.__checkForPoint__(point2)
        Plane.__checkForPoint__(point3)
        return Plane([point1, point2, point3])
    
    @staticmethod
    def get_plane_given_normal_vector_and_a_point(normal_vector, point):
        Plane.__checkForPoint__(point)
        Plane.__checkForVector__(normal_vector)
        return Plane([normal_vector,point])
    
    def __get_plane_passing_through_3_points__(self,point1, point2, point3):
        """ Arguments: Here points are the tuples/lists of(coordinate in space)
            example: point1 = [1,2,3] # this mean x co-ordinate: 1, y co-ordinate: 2, z co-ordinate: 3
                OR   point1 = (1,2,3) # this mean x co-ordinate: 1, y co-ordinate: 2, z co-ordinate: 3
            same for point2 and point3
        """
        Plane.__checkForPoint__(point1)
        Plane.__checkForPoint__(point2)
        Plane.__checkForPoint__(point3)
        p1 = Vector(point1)
        p2 = Vector(point2)
        p3 = Vector(point3)
        p1p2 = p2 - p1
        p1p3 = p3 - p1
        normal_vector = p1p2 * p1p3       # Cross product of vector pip2 and p1p3
        constant = -p1.dot(normal_vector)
        self.normal_vector, self.constant = normal_vector, constant
        #return Plane((normal_vector, constant))
    
    #@staticmethod
    def __get_plane_given_normal_vector_and_a_point__(self,normal_vector, point):
        """ 
            Arguments:
            normal_vector (object of class Vector) is a vector normal to the plane
            point is a tuples/lists of(coordinate in space)
            example: point = [1,2,3] # this mean x co-ordinate: 1, y co-ordinate: 2, z co-ordinate: 3
                OR   point = (1,2,3) # this mean x co-ordinate: 1, y co-ordinate: 2, z co-ordinate: 3
                     normal_vector = Vector([4,2,5])
        """
        Plane.__checkForPoint__(point)
        Plane.__checkForVector__(normal_vector)
        constant = -Vector(point).dot(normal_vector)
        self.normal_vector, self.constant = normal_vector, constant
        #return Plane((normal_vector, constant))
    
    @staticmethod
    def get_plane_through_intersection_of_planes_and_a_point(plane1, plane2, point):
        Plane.__checkForPlane__(plane1)
        Plane.__checkForPlane__(plane2)
        Plane.__checkForPoint__(point)
        vector = Vector(point)
        p1 = vector.dot(plane1.normal_vector) + plane1.constant
        p2 = vector.dot(plane2.normal_vector) + plane2.constant
        _lambda = -p1/p2
        v = plane1.normal_vector + plane2.normal_vector * _lambda
        v = v._vector_
        constant = plane1.constant + _lambda* plane2.constant
        v.append(constant)
        return Plane(v)

class Vector:
    
    def __init__(self, vector = None):
        if(vector == None): raise ValueError('Vector not specified')
        if(type(vector) != list and type(vector) != tuple): raise TypeError('Vector must be of type list')
        self._vector_ = list(vector)
    
    def __str__(self):
        s, axis = '', ord('i')
        for i in range(len(self._vector_) - 1):
            s = s + str(self._vector_[i]) + chr(axis)
            if(self._vector_[i+1] < 0): s += ' '
            else: s += ' +'
            axis += 1 
        s = s + str(self._vector_[i+1])  + chr(axis)
        return s
    
    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self,key):
        return self._vector_[key]
    
    def __len__(self):
        return len(self._vector_)
    
    def __add__(self, vector):
        Vector.__check_if_arg_is_vector__(vector)
        if(len(self._vector_) != len(vector)): raise ValueError("Dimentions to both vectors doesn't matches")
        add = []
        for i in range(len(vector)):
            add.append(self._vector_[i] + vector[i])
        return Vector(add)
    
    def __eq__(self, vector):
        Vector.__check_if_arg_is_vector__(vector)
        if(len(self._vector_) != len(vector)): raise ValueError("Dimentions to both vectors doesn't matches")
        for i in range(len(vector)):
            if(self._vector_[i] != vector[i]): return False
        return True
    
    def __sub__(self, vector):
        Vector.__check_if_arg_is_vector__(vector)
        if(len(self._vector_) != len(vector)): raise ValueError("Dimentions to both vectors doesn't matches")
        diff = []
        for i in range(len(vector)):
            diff.append(self._vector_[i] - vector[i])
        return Vector(diff)
    
    def __mul__(self,vector):
        if(vector.__class__.__name__ == Vector.__name__):
            return self.cross(vector)
        elif(type(vector) == int or type(vector) == float):
            return self.scale(vector)
        else:
            raise TypeError('Invalid argument arg. must be of' + str(Vector.__class__.__name__) +' or int or float')
    
    def __truediv__(self,scaler):
        if(scaler.__class__.__name__ == Vector.__name__):
            raise ValueError('Division of two vectors is not possible')
        elif(type(scaler) == int or type(scaler) == float):
            return self.scale(1/scaler)
        else:
            raise ValueError('Invalid argument')
    
    def __lt__(self,vector):
        Vector.__check_if_arg_is_vector__(vector)
        return (self.magnitude(self) < self.magnitude(vector))

    def __le__(self,vector):
        Vector.__check_if_arg_is_vector__(vector)
        return (self.magnitude(self) <= self.magnitude(vector))

    def __gt__(self,vector):
        Vector.__check_if_arg_is_vector__(vector)
        return (self.magnitude(self) > self.magnitude(vector))

    def __ge__(self,vector):
        Vector.__check_if_arg_is_vector__(vector)
        return (self.magnitude(self) >= self.magnitude(vector))

    def __ne__(self,vector):
        Vector.__check_if_arg_is_vector__(vector)
        return not self.__eq__(vector)

    def __neg__(self):
        l = []
        for i in range(len(self)):
            l.append(-self._vector_[i])
        return Vector(l)
    
    def copy(self):
        return Vector(self._vector_.copy())
    
    def magnitude(self, precision= 10):
        result = 0
        for c in self._vector_:
            result += c*c
        return sqrt(result)
    
    def dot(self, vector):
        Vector.__check_if_arg_is_vector__(vector)
        if(len(self._vector_) != len(vector)): raise ValueError("Dimentions to both vectors doesn't matches")
        ret = 0
        for i in range(len(vector)):
            ret += self._vector_[i] * vector[i]
        return ret
    
    def cross(self,vector):
        Vector.__check_if_arg_is_vector__(vector)
        if(len(self._vector_) != len(vector)): raise ValueError("Dimentions to both vectors doesn't matches")
        if(len(self._vector_) > 3 or len(vector) > 3): raise ValueError("Cross Products of Vectors in Higher Dimensional Euclidean Spaces is not implemented yet")
        vector1, vector2 = self.copy(), vector.copy()
        if(len(vector) == 2):
            vector1._vector_.append(0)
            vector2._vector_.append(0)
        l = []
        l.append(vector1[1] * vector2[2] - vector2[1] * vector1[2])
        l.append(-(vector1[0] * vector2[2] - vector2[0] * vector1[2]))
        l.append(vector1[0] * vector2[1] - vector2[0] * vector1[1])
        return Vector(l)
    
    def unit_vector(self):
        mag = self.magnitude()
        l = []
        for c in self._vector_:
            l.append(c/mag)
        return Vector(l)
    
    def angle(self,vector,unit='rad'):
        Vector.__check_if_arg_is_vector__(vector)
        if unit not in ['deg', 'rad']: raise ValueError("Unit can only be 'deg' or 'rad'")
        denominator = self.magnitude() * vector.magnitude()
        if denominator == 0: raise ZeroDivisionError('Undefined angle, zero-length vector is provided')
        radian = arccos(self.dot(vector)/denominator)
        if unit == 'deg':
            radian = radian * 180 / pi
        return radian

    def is_parallel_to_vector(self,vector):
        Vector.__check_if_arg_is_vector__(vector)
        ang = self.angle(vector)
        if(ang == 0): return True
        return False
    
    def is_perpendicular_to_vector(self,vector):
        Vector.__check_if_arg_is_vector__(vector)
        ang = self.angle(vector)
        if(ang == pi/2): return True
        return False
    
    def is_parallel_to_plane(self,plane):
        Vector.__check_if_arg_is_plane__(plane)
        return plane.is_parallel_to_vector(self)
    
    def is_perpendicular_to_plane(self,plane):
        Vector.__check_if_arg_is_plane__(plane)
        return plane.is_perpendicular_to_vector(self)
    
    def scale(self,scalingFactor):
        l = []
        for c in self._vector_:
            l.append(c*scalingFactor)
        return Vector(l)

    @staticmethod
    def volume(vector1, vector2, vector3):
        Vector.__check_if_arg_is_vector__(vector1)
        Vector.__check_if_arg_is_vector__(vector2)
        Vector.__check_if_arg_is_vector__(vector3)
        return vector1.dot(vector2*vector3)
    
    @staticmethod
    def area(vector1, vector2):
        Vector.__check_if_arg_is_vector__(vector1)
        Vector.__check_if_arg_is_vector__(vector2)
        return (vector1*vector2).magnitude()
    
    @staticmethod
    def get_plane_passing_through_3_points(point1, point2, point3):
        return Plane([point1,point2,point3])
    
    @staticmethod
    def get_plane_given_normal_vector_and_a_point(normal_vector, point):
        return Plane([normal_vector,point])
    
    @staticmethod
    def __check_if_arg_is_vector__(vector):
        if(vector.__class__.__name__ != Vector.__name__):
            raise TypeError("Argument must be of Type: "+str(Vector.__name__))
        
    @staticmethod
    def __check_if_arg_is_plane__(plane):
        if(plane.__class__.__name__ != Plane.__name__):
            raise TypeError("Argument must be of Type: "+str(Plane.__name__))
        
    
def getRandomVectors(n=5, dimentions = 3):
    from random import randrange
    ret = []
    for i in range(n):
        temp = []
        for j in range(dimentions):
            temp.append(randrange(-100,100))
        ret.append(temp)
    return ret
warnings.filterwarnings('ignore')

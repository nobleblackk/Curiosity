# 18.02 - Multivariable Calculus (Fall 2007)
This directory will contain some of the 18.02 content implemented in python
Inspired by MIT(Massachusetts Institute of Technology) course 18.02
https://ocw.mit.edu/courses/mathematics/18-02-multivariable-calculus-fall-2007/

			########### Beginning of 18.02 Implementation ############
			
- Vector: 2 classes Vector and Plane
Methods of class Vector: (Say you have two vectors v1, v2)
	- Creating a Vector object: 		Vector([8, 48, 33]) #   8i +48j +33k 
	- Vector addition: 			v1 + v2
	- Vector subtraction: 			v1 - v2
	- Vector Dot-Product			v1.dot(v2)
	- Vector Cross-Product			v1 * v2 OR v1.cross(v2)
	- Comparing magnitude: 			v1 < v2, v1 <= v2, v1 > v2, v1 >= v2
	- Check equallity of vectors:	 	v1 == v2, v1 != v2
	- Scaling vector: 			v1 * 2, v1 / 2 OR v1.scale(2), v1.scale(1/2) respectively
	- Negating Vector: 			-v1
	- Unit Vector: 				v1.unit_vector()
	- Angle b/w 2 vectors: 			v1.angle(v2)
	- Are vectors parallel: 		v1.is_parallel_to_vector(v2)
	- Are vector perpendicular:		v1.is_perpendicular_to_vector(v2)
	- Volume of a Parallelopiped		volume = Vector.volume(v1,v2,v3)
	- Area b/w 2 vectors: 			Vector.area(v1,v2)
	- Is vector parallel to plane		v1.is_parallel_to_plane(plane) # Here plane is object of class Plane
	- Is vector perpendicular to plane	v1.is_perpendicular_to_plane(plane) # Here plane is object of class Plane

Methods of class Plane: (Say you have a object of class Plane 'plane')
	- Create Plane object Given normal_vector, constant:		Plane([normal_vector,constant])
	- Create Plane object Given 3 points in space:			Plane([point1,point2,point3])
										# OR
							Plane.get_plane_passing_through_3_points(point1,point2,point3)
	- Create Plane object Given normal vector and a point:		Plane([normal_vector,point])
										# OR
							Plane.get_plane_given_normal_vector_and_a_point(normal_vector,point)
	- Create plane through intersection of 2 planes and point:	Plane.get_plane_through_intersection_of_planes_and_a_point(plane1,plane2,point)
	- Get Normal Vector and Constant of a Plane object: 		plane.get_normal_vector_and_constant()
	- Planes addition: 			plane1 + plane2
	- Planes subtraction: 			plane1 - plane2
	- Scaling of a Plane: 			plane * 2, plane / 2  OR plane.scale(2), plane.scale(1/2) respectively
	- Are planes parallel: 			plane1.is_parallel_to_plane(plane1)
	- Are planes perpendicular:		plane1.is_perpendicular_to_plane(plane1)
	- Is plane parallel to vector		plane1.is_parallel_to_vector(v1)
	- Is plane perpendicular to vector	plane1.is_perpendicular_to_vector(v1)
	- Angle b/w 2 planes:			plane1.angle(plane2)


				##### In Progress #####

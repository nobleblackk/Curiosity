# MIT OPENCOURSEWARE (python implementation)
This repository contains some of the MIT OCW courses content implemented in python(not entire course content)
Currntly it contains:

############ 6.006 - Introduction to Algorithms (Fall 2011)##############

				#### Beginning of 6.006 Implementation ####
	- Dynamic-Programming :-
		- Knapsack
		- Longest Increasing Subsequence
		- Parenthesization (Matrix chain multiplication)
		- Shortest Path (Minimum Weighted path from source to destination)
	- Graph :-
		- 2x2x2 Rubiks cube Solver
		- Graph Using Hash Table :-
			- Binary Heap (Used in Dijkstra)
			- Open Addressing: for Hash Table
			- Depth-First-Search: Used in method                AdjacencyList.isCycleExist() method
			- Breath-First-Search: Used in a method             __ShortestPath__.shortestPathWeighted() method
			- Topological Sort
			- Dijkstra Algorithm: Using HashTable in method:    __ShortestPath__.dijkstraV1()
			- Dijkstra Algorithm: Using Binary Heap in method:  __ShortestPath__.dijkstraV2()
			- Bellman-Ford in method:                           __ShortestPath__.bellman_ford()
		- Knapsack
	- Hashing :-
		- Pattern Searching Using Rabin-Karp Algorithm
		- Hash Table :-
			- Hash Table Using Chaining
			- Hash Table Using Open Addressing
	- Newton method for nth root
	- Peak Finding 3D
	- Heap Sort
				#### END of 6.006 Implementation ####
	
############ 18.02 - Multivariable Calculus (Fall 2007) ################

		#### Beginning of 18.02 Implementation ####
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
		- Create plane through intersection of 2 planes and point:	Plane.get_plane_through_intersection_of_planes_and_a_point(plane1,plane2,point)
		- Get Normal Vector and Constant of a Plane object: 		plane.get_normal_vector_and_constant()
											# OR
										Plane.get_plane_given_normal_vector_and_a_point(normal_vector,point)
		- Planes addition: 			plane1 + plane2
		- Planes subtraction: 			plane1 - plane2
		- Scaling of a Plane: 			plane * 2, plane / 2  OR plane.scale(2), plane.scale(1/2) respectively
		- Are planes parallel: 			plane1.is_parallel_to_plane(plane1)
		- Are planes perpendicular:		plane1.is_perpendicular_to_plane(plane1)
		- Is plane parallel to vector		plane1.is_parallel_to_vector(v1)
		- Is plane perpendicular to vector	plane1.is_perpendicular_to_vector(v1)
		- Angle b/w 2 planes:			plane1.angle(plane2)
		

					#### In Progress ####

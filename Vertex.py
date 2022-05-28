import math

class Vertex:
	
	# Vertex constructor
	def __init__(self, id, x=0, y=0):
		self.id = id
		self.x = x
		self.y = y
		self.adjacents = {}
		self.previous = None

	# Returns the id of the current vertex object
	def get_id(self):
		return self.id
	
	# Returns the x coordinate of the current vertex object
	def get_x(self):
		return self.x
	
	# Returns the y coordinate of the current vertex object
	def get_y(self):
		return self.y

	# Returns all neighbors of the current vertex object
	def get_adjacents(self):		
		return self.adjacents.keys()
	
	# Returns the auxiliar attribute of previous vertex to backtrack
	#   when computing the shortest path with Dijsktra's algorithm
	def get_previous(self):
		return self.previous

	# Set 'vertex' as a neighbor of the current node with
	#   weight equal to the provided 'distance'
	def add_adjacent(self, vertex, distance):
		self.adjacents[vertex] = distance
	
	# Removes provided 'vertex' as a neighbor of the current vertex
	#   (removes edge between them)
	def remove_adjacent(self, vertex):
		if self.is_adjacent_to(vertex):
			del self.adjacents[vertex]

	# Returns the distance/weight of the edge between the current
	#   vertex and the provided 'vertex'
	def get_distance(self, vertex):		
		return self.adjacents[vertex]
	
	# Calculates the euclidean distance between the current
	#   vertex and the provided 'vertex'
	def get_euclidean_distance(self, vertex):
		dx = self.x - vertex.x
		dy = self.y - vertex.y
		return math.sqrt(dx**2 + dy**2)

	# Returns True if the provided 'vertex' is a neighbor of the
	#   current vertex (if they are connected by an edge)
	def is_adjacent_to(self, vertex):
		return vertex in self.adjacents
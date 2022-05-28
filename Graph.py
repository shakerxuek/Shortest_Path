import os
from Vertex import Vertex


class Graph:
	
	# Graph constructor
	def __init__(self, vertex_file=None, edge_file=None):
		self.vertices = {}
		
		if vertex_file != None and edge_file != None:
			self.load_graph(vertex_file, edge_file)

	# Adds vertex to the graph
	def add_vertex(self, vertex_id, x=0, y=0):
		vertex = Vertex(vertex_id, x, y)
		self.vertices[vertex_id] = vertex

	# Returns vertex object based on its id
	def get_vertex(self, vertex_id):
		return self.vertices[vertex_id]

	# Returns True if the graph contains a vertex with the given id
	def has_vertex(self, vertex_id):
		return vertex_id in self.vertices

	# Creates an edge between two vertices (the vertices must already exist!)
	def add_edge(self, src_id, dest_id, distance=1, undirected=True, euclidean=False):	
		if euclidean:
			distance = self.vertices[src_id].get_euclidean_distance(self.vertices[dest_id])
		
		self.vertices[src_id].add_adjacent(self.vertices[dest_id], distance)
		if undirected:
			self.vertices[dest_id].add_adjacent(self.vertices[src_id], distance)

	# Returns True if the graph contains an edge between the given vertices ids
	def has_edge(self, src_id, dest_id):
		return self.vertices[src_id].is_adjacent_to(self.vertices[dest_id])

	# Returns an iterator of all vertices in the graph
	def get_vertices(self):
		return iter(self.vertices.values())
	
	# Auxiliar function to create graph based on edge and vertex files (of Calgary road network)
	def load_graph(self, vertex_file, edge_file):
		try:
			# Make sure files exist
			if not os.path.isfile(vertex_file) or not os.path.isfile(edge_file):
				raise Exception('File not found!')
			
			# Reading vertex file and adding vertices to graph
			with open(vertex_file, 'r') as f:
				line = f.readline()
				while line:
					line = line.split('\t')
					self.add_vertex(int(line[0]), float(line[1]), float(line[2]))
					line = f.readline()
			
			# Reading edge file and adding edges to graph
			with open(edge_file, 'r') as f:
				line = f.readline()
				while line:
					line = line.split('\t')
					self.add_edge(int(line[0]), int(line[1]), euclidean=True)
					line = f.readline()
		except Exception as e:
			print(e)
			return False

		return True
	
	# Auxiliar function to create an adjacency matrix (dictionary, really) of current graph
	def get_adjacency_matrix(self):
		matrixDict = {}
		allVertices = list(self.get_vertices())
		allVerticesIds = [v.get_id() for v in allVertices]
		
		for vertex in allVertices:
			adjacents = list(vertex.get_adjacents())		
			adj_dist = {v:vertex.get_distance(v) for v in adjacents}
			matrixDict[vertex.get_id()] = [str(adj_dist[v]) if v in adjacents else '0' for v in allVertices]
		
		return allVerticesIds, matrixDict
	
	# Prints the adjacency matrix of current graph
	def print_adjacency_matrix(self):
		v_separator = '\t'
		tabSize = 4
		
		vertices, matrix = self.get_adjacency_matrix()
		
		if len(vertices) == 0:
			return
		
		tmpStr = v_separator + v_separator.join(vertices)
		print(tmpStr.expandtabs(tabSize))
		print('-' * tabSize * (len(vertices) + 1))
		
		for vertex in vertices:
			tmpStr = vertex + v_separator + v_separator.join(matrix[vertex])
			print(tmpStr.expandtabs(tabSize))

	# Auxiliar function to create an adjacency list (dictionary, really) of current graph
	def get_adjacency_list(self):
		verticesDict = {}
		allVertices = list(self.get_vertices())
		allVerticesIds = [v.get_id() for v in allVertices]
		
		for vertex in allVertices:
			adjacents = list(vertex.get_adjacents())
			verticesDict[vertex.get_id()] = {v.get_id():vertex.get_distance(v) for v in adjacents}
		
		return allVerticesIds, verticesDict

	# Prints the adjacency list of current graph
	def print_adjacency_list(self):
		v_separator = '\t'
		tabSize = 4
		
		vertices, dict = self.get_adjacency_list()
		
		if len(vertices) == 0:
			return
		
		for key, value in dict.items():
			tmpStr = key + ':' + v_separator + str(value)
			print(tmpStr.expandtabs(tabSize))
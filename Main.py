from Graph import Graph
import pandas
import heapq



# part1
graph1=Graph()

graph1.add_vertex('v1')
graph1.add_vertex('v2')
graph1.add_vertex('v3')
graph1.add_vertex('v4')
graph1.add_vertex('v5')
graph1.add_vertex('v6')
graph1.add_vertex('v7')

graph1.add_edge('v1','v2',3)
graph1.add_edge('v1','v3',5)
graph1.add_edge('v2','v4',7)
graph1.add_edge('v2','v5',3)
graph1.add_edge('v5','v6',8)
graph1.add_edge('v4','v7',10)

graph2=Graph()

graph2.add_vertex('a')
graph2.add_vertex('b')
graph2.add_vertex('c')
graph2.add_vertex('d')
graph2.add_vertex('e')
graph2.add_vertex('f')
graph2.add_vertex('g')
graph2.add_vertex('h')


graph2.add_edge('b','d')
graph2.add_edge('a','d')
graph2.add_edge('d','g')
graph2.add_edge('a','e')
graph2.add_edge('e','h')
graph2.add_edge('g','e')
graph2.add_edge('f','b')
graph2.add_edge('c','b')
graph2.add_edge('d','c')
graph2.add_edge('c','a')
graph2.add_edge('a','b')
def BFS(graph,src_id):
	Q=[]
	V=[]
	Q.append(src_id)
	while Q:
		Temp=Q[0]
		Q.pop(0)
		V.append(Temp)
		a=graph.get_vertex(Temp)
		b=a.get_adjacents()
		num=list(b)
		for i in num:
			r=i.get_id()
			if (r not in Q) and (r not in V):
				Q.append(r)
	return V

def DFS(graph,src_id):
	S=[]
	V=[]
	S.append(src_id)
	while S:
		Temp=S[0]
		S.pop(0)
		V.append(Temp)
		a=graph.get_vertex(Temp)
		b=a.get_adjacents()
		num=list(b)
		for i in num:
			r=i.get_id()
			if (r not in S) and (r not in V):
				S.insert(0,r)
	return V

# 1)
# print(BFS(graph1,'v1'))
# print(DFS(graph1,'v1'))

# # 2)
print(BFS(graph2,'c'))
print(DFS(graph2,'c'))

# 3)
# BFS stands for Breadth First Search is a vertex based technique for finding a shortest path in graph. 
# It uses a Queue data structure which follows first in first out. 
# In BFS, one vertex is selected at a time when it is visited and marked then its adjacent are visited and stored in the queue. It is slower than DFS. 
# DFS stands for Depth First Search is a edge based technique. 
# It uses the Stack data structure, performs two stages, first visited vertices are pushed into stack and second if there is no vertices then visited vertices are popped. 


# part2

def shortest_path(graph,src_id,des_id):
	Q=[]
	for i in graph.get_vertices():
		Q.append(i.get_id())
	dist={n:float('inf') for n in Q}
	dist[src_id]=0
	visited=[]
	output=[]
	V=[(0,src_id)]

	while len(V)>0:
		# print(V)
		cdist,cvertex=heapq.heappop(V)
		visited.append(cvertex)
		# print('out',cdist)
		# print('outid',cvertex)

		if cdist>dist[cvertex]:
			continue
		for i in (list((graph.get_vertex(cvertex)).get_adjacents())):
			i=i.get_id()
			# print(i)
			nm=(graph.get_vertex(cvertex)).get_distance((graph.get_vertex(i)))
			# print(nm)
			temp=cdist+nm
			# print(temp)
			if temp<dist[i]:
				dist[i]=temp
				(graph.get_vertex(i)).previous=cvertex
				heapq.heappush(V,(temp,i))
			if i==des_id:
				print(i)
				found=i	
				output.append(found)
				while (graph.get_vertex(found)).previous != None:
					tem=(graph.get_vertex(found)).previous
					output.append(tem)
					found=tem
	output.reverse()
	return dist[des_id],output

vertax_file='Data/Vertex.txt'
edge_file='Data/edge.txt'

graph=Graph(vertax_file,edge_file)



			
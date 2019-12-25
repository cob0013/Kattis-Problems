from queue import PriorityQueue
import sys
class Dijkstras:
	def __init__(self, verts, graph):
		self.V  = verts
		self.graph = graph
	def minDistance(self, dist, sptSet):
		min = 99999999
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v
		return min_index
	def dijsktras(self, src):
		dist = [99999999] * self.V
		dist[src] = 0
		sptSet = [False] * self.V
		for i in range(self.V):
			u = self.minDistance(dist, sptSet)
			sptSet[u] = True
			for v in range(self.V):
				if self.graph[u][v] > 0 and sptSet[v] == False \
				and dist[v] > dist[u] + self.graph[u][v]:
					dist[v] = dist[u] + self.graph[u][v]
		return dist

	


n, s, t = map(int, input().split())
graph = []
for i in range(n):
	row = list(map(int, input().split()))
	graph.append(row)
d = Dijkstras(n, graph)
print(d.dijsktras(s)[t])





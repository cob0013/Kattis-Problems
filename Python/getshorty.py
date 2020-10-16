import sys
from queue import PriorityQueue

class Graph:
	def __init__(self, vertices):
		self.graph = [[] for i in range(vertices)]
		self.vertices = vertices

	def dijkstra(self):
		size = [0.0 for i in range(self.vertices)]
		q = PriorityQueue()
		spt = [False] * self.vertices
		q.put((-1, 0))
		while not q.empty():
			f, vert = q.get()
			if spt[vert]:
				continue
			spt[vert] = True
			f *= -1
			size[vert] = f
			for neighbors in self.graph[vert]:
				fact = neighbors[1]
				_next = neighbors[0]
				q.put((-1* f * fact, _next))
		return size





def main():
	n, m = map(int, input().split())
	while n != 0 and m != 0:
		graph = Graph(n)
		for i in range(m):
			line = input().split()
			u = int(line[0])
			v = int(line[1])
			f = float(line[2])
			graph.graph[v].append((u, f))
			graph.graph[u].append((v, f))

		print('%.4f' %graph.dijkstra()[n - 1])
		n, m = map(int, input().split())
if __name__ == "__main__":
	main()





		

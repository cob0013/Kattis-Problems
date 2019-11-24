### not finished giving wrong result for somereason

class Graph():
	def __init__(self, vertices, g):
		self.V = vertices
		self.graph = g
	def minKey(self, key, mstSet):
		_min = 99999999
		for v in range(self.V):
			if key[v] < _min and mstSet[v] == False:
				_min = key[v]
				min_index = v
		return min_index

	def prims(self):
		key = [99999999] * self.V
		parent = [None] * self.V
		key[0] = 0
		mstSet= [False] * self.V
		parent[0] = -1
		for cout in range(self.V):
			u = self.minKey(key, mstSet)
			mstSet[u] = True
			for v in range(self.V):
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u

		for i in range(1, self.V):
			print(parent[i], i)

def main():
	n, m = map(int, input().split())
	graph = []
	for i in range(n):
		graph.append([0 for j in range(n)])
	for i in range(m):
		v1, v2, d = map(int, input().split())
		graph[v1][v2] = d
		graph[v2][v1] = d
	print(graph)
	g = Graph(n, graph)

	g.prims()
if __name__ == "__main__":
	main()
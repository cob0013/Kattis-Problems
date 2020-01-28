import heapq

def prims(graph, n ):
	mst = {i : [] for i in range(n)}
	visited = set()
	visited.add(0)
	edges = []
	for i in range(n):
		neighbors = graph[i]
		for neigh in neighbors:
			v, w = graph[i]
			edges.appned(((w, i, v)))
	heapq.heapify(edges)
	while len(visited) != n:
		weight, frm, to = heapq.heappop(pq)
		visited.add(from)


def main():
	while True:
		n, m = map(int, input().split())
		if n == m == 0:
			return
		graph = {i : [] for i in range(n)}
		for i in range(m):
			u, v, w = map(int, input().split())
			graph[u].append((v, w))
			graph[v].append((u, w))




if __name__ == "__main__":
	main()
from queue import PriorityQueue
def main():
	while True:
		n, m, q, s = map(int, input().split())
		if n == m == q == s == 0:
			break
		graph = {i : [] for i in range(n)}
		for i in range(m):
			u, v, w = map(int, input().split())
			graph[u].append((w, v))
		# dijkstras
		pq = PriorityQueue()
		visited = set()
		pq.put((0, s))
		dist = [-1 for i in range(n)]
		while not pq.empty():
			weight, vert = pq.get()
			if vert in visited:
				continue
			visited.add(vert)
			dist[vert] = weight
			for neighbor in graph[vert]:
				edgelength, goingto = neighbor
				if goingto not in visited:
					pq.put((edgelength + weight, goingto))
		for i in range(q):
			destination = int(input())
			if dist[destination] == -1:
				print("Impossible")
			else:
				print(dist[destination])
		print()




if __name__ == "__main__":
	main()
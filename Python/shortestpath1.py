import heapq
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
		pq = [(0, s)]
		visited = set()
		dist = [-1 for i in range(n)]
		while pq:
			weight, vert = heapq.heappop(pq)
			if vert in visited:
				continue
			visited.add(vert)
			dist[vert] = weight
			for neighbor in graph[vert]:
				edgelength, goingto = neighbor
				if goingto not in visited:
					heapq.heappush(pq, (edgelength + weight, goingto))
		for i in range(q):
			destination = int(input())
			if dist[destination] == -1:
				print("Impossible")
			else:
				print(dist[destination])
		print()




if __name__ == "__main__":
	main()
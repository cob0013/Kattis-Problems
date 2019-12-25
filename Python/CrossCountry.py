from queue import PriorityQueue
# re wrote cleaner but slower dijkstra's
def main():
	n, s, t = map(int, input().split())
	graph = []
	pq = PriorityQueue()
	pq.put((0, s))
	visited = set()
	for i in range(n):
		# adj matrix
		graph.append(list(map(int, input().split())))
	while pq:
		weight, vert = pq.get()
		visited.add(vert)
		if vert == t:
			print(weight)
			return
		for neigh in range(n):
			if neigh not in visited:
				pq.put((weight + graph[vert][neigh], neigh))


if __name__ == "__main__":
	main()
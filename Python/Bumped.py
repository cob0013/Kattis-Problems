import heapq

def dijkstras(graph, s, t, n):
	mx = 9999999
	dist = [mx] * 50
	minHeap = [(s, 0)]
	while minHeap:
		city, weight = heapq.heappop(minHeap)
		if dist[city] == mx:
			dist[city] = weight
			for dest in graph[city]:
					if dist[dest[0]] == mx:
						heapq.heappush(minHeap, (weight + dest[1], dest[0]))





def main():
	n, m, f, s, t = map(int, input().split())
	graph = dict()
	for i in range(n):
		graph[i] = []
	for i in range(m):
		a, b, c = map(int, input().split())
		graph[a].append((b, c))
		graph[b].append((a, c))
	for i in range(f):
		u, v = map(int, input().split())
		if u not in graph:
			graph[u] = []
		if v not in graph:
			graph[v] = []
		graph[u].append((v, 0))
		graph[v].append((u, 0))
		print(graph)
	dist = dijkstras(graph, s, t, n)
	# print(dist[t])








if __name__ == "__main__":
	main()
import heapq
def dijstras(graph, src, n):
	mx = 99999999
	dist = [mx for i in range(n)]
	pq = [(0, src)]
	while pq:
		weight, city = heapq.heappop(pq)
		if dist[city] == mx:
			dist[city] = weight
			for dest in graph[city]:
				if dist[dest] == mx:
					heapq.heappush(pq, (weight + graph[city][dest], dest))
	return dist
def main():
	n, m, f, s, t = map(int, input().split())
	graph = [dict() for i in range(n)]
	for i in range(m):
		x, y, z = map(int, input().split())
		graph[x][y] = z
		graph[y][x] = z
	flights = []
	for i in range(f):
		flights.append(list(map(int, input().split())))
	distanceTo = dijstras(graph, s, n)
	distanceFrom = dijstras(graph, t, n)
	minDistance = distanceTo[t]
	for flight in flights:
		minDistance = min(distanceTo[flight[0]] + distanceFrom[flight[1]], minDistance)
	print(minDistance)












if __name__ == "__main__":
	main()
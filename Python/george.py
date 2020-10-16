import heapq
# not finished


def waittime(u, v, time, blocked):
	wait = 0
	if (u, v) in blocked and blocked[(u, v)][0] <= time and blocked[(u, v)][1] > time:
		wait = blocked[(u, v)][1] - time
	return wait


def dijkstras(graph, src, going, blocked, n, time):
	visited = set()
	pq = [(time, src)]
	while pq:
		time, corner = heapq.heappop(pq)
		if corner == going:
			return time
		if corner in visited:
			continue
		visited.add(corner)
		for i in range(n + 1):
			if i not in visited  and i in graph[corner]:
				heapq.heappush(pq, ((waittime(corner, i, time, blocked) + time + graph[corner][i]), i)) 
	return -1


def main():
	n, m = map(int, input().split())
	a, b, k, g = map(int, input().split())
	graph = [dict() for i in range(n + 1)]
	george = list(map(int, input().split()))
	blockedtimes = dict()
	for i in range(m):
		a, b, l = map(int, input().split())
		graph[a][b] = l
		graph[b][a] = l

	enter = 0
	# for i in range(g - 1):
	# 	entering = timesofar
	# 	leaving = timesofar + graph[george[i]][george[i + 1]]
	# 	blockedtimes[(george[i], george[i + 1])] = (entering, leaving)
	# 	blockedtimes[(george[i + 1], george[i])] = (entering, leaving)
	# 	timesofar = leaving



		
   


		
	print(dijkstras(graph, a, b, blockedtimes, n, k))






if __name__ == "__main__":
	main()
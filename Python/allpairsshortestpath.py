import heapq
import sys
# not finished
INF = 9999999
def floydwarshall(graph, v):
	dist = graph.copy()

	for k in range(v):
		for i in range(v):
			for j in range(v):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
	return dist




def main():
	output = []
	while True:
		
			n, m, q = map(int, sys.stdin.readline().split())

			if n == m == q == 0:
				print("\n".join(output))
				return
			graph = [[INF for i in range(n)] for i in range(n)]
			for i in range(m):
				u, v, w = map(int, sys.stdin.readline().split())
				graph[u][v] = w
			for i in range(n):
				graph[i][i] = 0
			shortestpaths = floydwarshall(graph, n)
			for i in range(q):
				start, goal = map(int, sys.stdin.readline().split())
				shortest = shortestpaths[start][goal]
				if shortest == INF and graph[goal][start]:
					output.append("Impossible")
				elif shortestpaths[start][start] < 0 or shortestpaths[goal][goal] < 0:
					output.append("-Infinity")
				else:
					output.append(str(min(graph[start][goal], graph[goal][start])))
			output.append("")

				

		



if __name__ == "__main__":
	main()
# not finished

from collections import deque 

def dfs(graph, start, visited):
	visited.add(start)
	for neighbor in graph[start]:
		if neighbor in visited:
			return True
		visited.add(neighbor)
		if dfs(graph, neighbor, visited):
			return True
		visited.remove(neighbor)
	return False
	


def main():
	n = int(input())
	graph = dict()
	visited = set()
	for i in range(n):
		u, v = input().split()
		if u not in graph:
			graph[u] = set()
		if v not in graph:
			graph[v] = set()
		graph[u].add(v)

	while True:
		try:
			check = input()
			if dfs(graph, check, visited):
				print(check, "safe")
			else:
				print(check, "trapped")
		except:
			return
		
		


if __name__ == "__main__":
	main()
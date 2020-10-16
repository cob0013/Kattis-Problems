# not finished
import sys 

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
	lines = [i.strip() for i in sys.stdin.readlines()]
	n = int(lines[0])
	graph = dict()
	for i in range(1,n + 1):
		u, v = lines[i].split()
		if u not in graph:
			graph[u] = set()
		if v not in graph:
			graph[v] = set()
		graph[u].add(v)

	for i in range(n + 1, len(lines)):
			visited = set()
			print(lines[i], "safe" if dfs(graph, lines[i], visited) else "trapped") 
		


if __name__ == "__main__":
	main()

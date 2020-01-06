from collections import deque
import math
def main():
	c, p, x, l = map(int, input().split())
	graph = {i : [] for i in range(1, c + 1)}
	left = dict()
	for i in range(p):
		u, v = map(int,input().split())
		graph[u].append(v)
		graph[v].append(u)
	for key in graph:
		left[key] = (math.ceil(len(graph[key]) / 2))
	left[l] = 0
	q = deque([l])
	while q:
		curr = q.pop()
		for partner in graph[curr]:
			left[partner] -= 1
			if left[partner] == 0:
				q.appendleft(partner)
	if left[x] <= 0:
		print("leave")
	else:
		print("stay")
	




if __name__ == "__main__":
	main()
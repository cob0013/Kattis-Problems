
# r1 * c + c1
from sys import stdin
from heapq import heappush, heappop, heapify

def main():
	r, c = map(int, stdin.readline().split())
	pq = []
	neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	visited = set()
	max_debth = -1
	grid = []
	for i in range(r):
		grid.append(list(map(int, stdin.readline().split())))
		heappush(pq, ((grid[i][0], i, 0)))
		visited.add(i * c)
	while pq:
		debth, x, y = heappop(pq)
		max_debth = max(max_debth, debth)
		if y == c - 1:
			print(max_debth)
			return
		for n in neighbors:
			iprime = x + n[0]
			jprime = y + n[1]
			if iprime < 0 or jprime < 0 or iprime >= r or jprime >= c or iprime * c + jprime  in visited:
				continue
			heappush(pq, ((grid[iprime][jprime], iprime, jprime)))
			visited.add(iprime * c + jprime)
			
			





	


if __name__ == "__main__":
	main()
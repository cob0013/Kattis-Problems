# rewrote islands 3 to work on uf
def union(parents, x, y):
	parents[find(parents, y)] = find(parents, x)

def find(parents, child):
	if parents[child] == child:
		return child
	parents[child] = find(parents, parents[child])
	return parents[child]
def main():
	r, c = map(int, input().split())
	connections = list(range(r * c))
	grid = []
	for i in range(r):
		grid.append(input())
	for i in range(r):
		for j in range(c):

			if i < r - 1 and (grid[i][j] == "C" or grid[i][j] == "L") and  (grid[i + 1][j] == "C" or grid[i + 1][j] == "L"):
				union(connections, i * c + j, (i + 1) * c + j)
			if j < c - 1  and (grid[i][j] == "C" or grid[i][j] == "L") and  (grid[i][j + 1] == "C" or grid[i][j + 1] == "L"):
				union(connections, i * c + j, i * c +( j + 1))
	check = set()
	for i in range(r):
		for j in range(c):
			if grid[i][j] == "L":
				check.add(find(connections, i * c + j))
	print(len(check))

if __name__ == "__main__":
	main()
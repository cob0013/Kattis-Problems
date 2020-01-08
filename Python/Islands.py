import collections
def dfs(r, c):
	stack = collections.deque()
	stack.append((r, c))
	grid[r][c] = "W"
	while stack:
		curr = stack.pop()
		for x, y in [(curr[0] + 1, curr[1]), (curr[0] - 1, curr[1]), (curr[0], curr[1] + 1), (curr[0], curr[1] - 1)]:
			if 0 <= x < rMax and 0 <= y < cMax and grid[x][y] != "W":
				grid[x][y] = "W"
				stack.append((x, y))

rMax, cMax = map(int, input().split())
grid = []
count = 0

for i in range(rMax):
	grid.append(list(input()))
for i in range(rMax):
	for j in range(cMax):
		if grid[i][j] == "L":
		
			dfs(i, j)
			count += 1


print(count)


# code was bad so re wrote cleaner


def find(parents, child):
	if parents[child] == child:
		return child
	parents[child] = find(parents, parents[child])
	return parents[child]
def union(parents, childX, childY):
	parents[find(parents,childY)] = find(parents,childX)

def main():
	r, c = map(int, input().split())
	grid = list()
	connections = list(range(c * r))
	for i in range(r):
		grid.append(input())
	for i in range(r):
		for j in range(c):
			if i < r - 1 and grid[i][j] == grid[i + 1][j]:
				union(connections, i * c + j, (i + 1) * c + j)
			if j < c - 1 and grid[i][j] == grid[i][j + 1]:
				union(connections, i * c + j, i * c + j + 1)
	check = int(input())
	for i in range(check):
		r1, c1, r2, c2 = map(int, input().split())
		r1 -= 1
		c1 -= 1
		r2 -= 1
		c2 -= 1
		if  find(connections,r1 * c + c1) == find(connections, r2 * c + c2):
			if grid[r1][c1] == "1":
				print("decimal")
			else:
				print("binary")

		else:
			print("neither")

if __name__ == "__main__":
	main()


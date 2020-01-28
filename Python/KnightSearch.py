from sys import stdin


# gross neighborsj
# i * n + j
# too slow python

def getNeigbors(i, j, n):
	neigbors = []
	output = []
	neigbors.append((i + 1, j + 2))
	neigbors.append((i - 1, j + 2))
	neigbors.append((i + 1, j - 2))
	neigbors.append((i - 1, j - 2))
	neigbors.append((i + 2, j + 1))
	neigbors.append((i - 2, j + 1))
	neigbors.append((i + 2, j - 1))
	neigbors.append((i - 2, j - 1))
	for nei in neigbors:
		x, y = nei
		if x >= 0 and y >= 0 and x < n and y < n:
			output.append(nei)
	return output



		



def main():
	n = int(input())
	visited = set()
	it = 0
	goal = "ICPCASIASG"
	grid = stdin.readline()
	for l in range(n * n):
			
			if grid[l] == "I":
				# enter dfs
# i * n + j
				i = l // n
				j = l - (i * n)
				stack = []
				count = 0
				stack.append((i, j, count))
				while stack:
					i, j, count = stack.pop()
					if grid[i * n  + j] == goal[count]:
						count += 1
					if count == len(goal):
						print("YES")
						return
			
					for neigh in getNeigbors(i, j, n):
						iprime, jprime = neigh
						if grid[iprime * n + jprime] == goal[count]:
							stack.append((neigh[0], neigh[1], count))	
	print("NO")
				

			




if __name__ == "__main__":
	main()
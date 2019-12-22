def manhattandist(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1] )
def main():
	board = []
	desired = []
	home = {}
	distance = 0
	desired.append("ABCD")
	desired.append("EFGH")
	desired.append("IJKL")
	desired.append("MNO.")
	for i in range(4):
		for j in range(4):
			home[desired[i][j]] = (i , j)

	for i in range(4):
		line = input()
		for j in range(4):
			if line[j] =='.':
				continue

			distance += manhattandist((i, j), home[line[j]])
	print(distance)


if __name__ == "__main__":
	main()
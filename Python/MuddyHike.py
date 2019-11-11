
# r1 * c + c1
from queue import deque
def main():
	r, c = map(int, input().split())
	grid = []
	dr = [1, -1, 0, 0]
	dc = [0, 0, 1, -1]
	for i in range(r):
		grid.append(list(map(int, input().split())))
	dist = [[999999999 for i in range(c + 2)] for i in range(r + 2)]
	for i in range(r):
		dist[r][0] = -1
	q = deque()
	q.append((0, 0, 0))
	dist[0][0] = 0
	while not q.empty():
		r, c , debth = q.popleft()
		for i in range(4):
			nextR = r + dr[i]
			nextC = c + dc[i]
		if nextR >= 0 and nextC >= 0 and nextR < r + 2 and nextC < c + 2:
			nextVal = max(debth, )

		spt[r][c] = True
		dist[r][c] = debth


	


if __name__ == "__main__":
	main()
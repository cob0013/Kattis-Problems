import math
def distance(p1, p2):
	return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))


def union(x, y, parents):
	parentX = find(x, parents)
	parentY = find(y, parents)
	parents[parentY] = parentX


def overlapping(p1, p2):
	return distance(p1, p2) < p1[2] + p2[2]


def find(child, parents):
	if parents[child] == child:
		return child
	parents[child] = find(parents[child], parents)
	return parents[child]

def leftEdge(field):
	return field[0] - field[2] < 0

def rightEdge(field):
	return field[0] + field[2] > 200


def main():
	n = int(input())
	unions = [i for i in range(n + 2)]
	fields = []
	for i in range(n):
		x, y, r = map(int, input().split())
		fields.append((x, y, r))
	for i in range(n):
		curr = fields[i]
		for j in range(i + 1):
			if overlapping(fields[i], fields[j]):
				union(i + 1, j + 1, unions)
		if rightEdge(curr):
			union(n + 1, i + 1, unions)
		if leftEdge(curr):
			union(0, i + 1, unions)
		if find(0, unions) == find(n + 1, unions):
				print(i)
				break


		

if __name__ == '__main__':
	main()
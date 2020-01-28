def find(parents, child):
	if parents[child] == child:
		return child
	parents[child] = find(parents, parents[child])
	return parents[child]
def union(parents, childX, childY):
	parentX = find(parents, childX)
	parentY = find(parents, childY)
	parents[parentY] = parentX
def main():
	n, q = map(int, input().split())
	parents = list(range(n))
	for i in range(q):
		op, x, y = input().split()
		x = int(x)
		y = int(y)
		if op == '=':
			union(parents, x, y)
		else:
			if find(parents, x) == find(parents, y):
				print("yes")
			else:
				print("no")
if __name__ == "__main__":
	main()
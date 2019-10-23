def find(parents, child):
	if parents[child] == child:
		return child
	parents[child] = find(parents, parents[child])
	return parents[child]
def union(parents, x, y):
	parentX = find(parents, x)
	parentY = find(parents, y)
	parents[parentY] = parentX
line = input().split()
houses = int(line[0])
cables = int(line[1])
parents = [None] * houses
for i in range(len(parents)):
	parents[i] = i
for i in range(cables):
	l = input().split()
	union(parents, int(l[0]) - 1, int(l[1]) - 1)
works = True
check = find(parents, 0)
for i in range(1, len(parents)):
	if check != find(parents, i):
		print(i + 1)
		works = False

if works:
	print("Connected")


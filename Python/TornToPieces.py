n = int(input())
routes = dict()
visited = dict()
traceBack = dict()
path = list()
for i in range(n):
	l = input().split()
	for x in l:
		if x in routes:
			routes[x].append(l)
		else: 
			routes[x] = l
		visited[x] = False

last = input().split()
stack = []
start = last[0]
end = last[1]
curr = start
path.append(start)
stack.append(curr)
while curr != end and len(stack) != 0:
		curr = stack.pop()
		visited[curr] = True
		for x in routes:
			if not visited[x]:
				stack.append(x)
				path.append(x)
			else:
				if x in path:
					path.remove(x)

if curr == end:
	print(path)









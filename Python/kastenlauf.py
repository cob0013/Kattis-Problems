
def dist(c1, c2):
	return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
def dfs(start, finish, stores):
	stack = [start]
	visited = set()
	visited.add(start)
	while stack:
		x, y = stack.pop()
		if dist((x, y), finish) <= 1000:
			return True
		for store in stores:
			if dist((x, y), store) <= 1000 and store not in visited:
				stack.append(store)
				visited.add(store)
	return False

def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		stores = []
		start = tuple(map(int, input().split()))
		for i in range(n):
			x, y = map(int, input().split())
			stores.append((x, y))
		end = tuple(map(int, input().split()))
		if dfs(start, end, stores):
			print('happy')
		else:
			print('sad')



if __name__ == '__main__':
	main()
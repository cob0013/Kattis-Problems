from sys import stdin
def find(parents, child):
	if parents[child] == child:
		return child
	parents[child] = find(parents, parents[child])
	return parents[child]
def union(parents, childX, childY):
	parents[find(parents,childY)] = find(parents,childX)

def main():
	output = []
	n = int(input())
	for i in range(n):
		m = int(stdin.readline())
		unions = [j for j in range(m)]
		r = int(stdin.readline())
		for k in range(r):
			u, v = map(int, stdin.readline().split())
			union(unions, u, v)
		count = set()
		for u in unions:
			count.add(find(unions, u))
		output.append(str(len(count) - 1))
	print("\n".join(output))


if __name__ == "__main__":
	main()
# 2
# 5
# 3
# 0 1
# 1 2
# 3 4
# 2
# 1
# 0 1

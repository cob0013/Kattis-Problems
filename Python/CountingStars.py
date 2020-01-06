def find(parents, child):
	if parents[child] == child:
		return child
	parents[child] = find(parents, parents[child])
	return parents[child]

def union(parents, childx, childy):
	parents[find(parents,childy)] = find(parents,childx)


def main():
	count = 1
	while True:
		try:
			m, n = map(int, input().split())
			unions = [i for i in range(n * m)]
			stars = set()
			image = []
			for i in range(m):
				image.append(input())
			for i in range(m):
				for j in range(n):
					if image[i][j] == "-":
						# check right
						if j < n - 1 and image[i][j + 1] == "-":
							union(unions, i * n + j, i * n + j + 1)
						# check below
						if i < m - 1 and image[i + 1][j] == "-":
							union(unions, i * n + j, (i + 1) * n + j)
			for i in range(m):
				for j in range(n):
					if image[i][j] == "-":
						stars.add(find(unions, i * n + j))
			print("Case " + str(count) + ": " + str(len(stars)))
			count += 1
		except:
			return
		
			

if __name__ == "__main__":
	main()


def main():
	n = int(input())
	langs = input().split()
	dist = {}
	_min = n
	for i in range(n):
		if langs[i] in dist:
			_min = min(i - dist[langs[i]] , _min)
		dist[langs[i]] = i
	print(_min)

if __name__ == '__main__':
	main()


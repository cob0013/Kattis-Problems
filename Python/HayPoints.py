def main():
	hay = dict()
	m, n = map(int, input().split())
	for i in range(m):
		word, val = input().split()
		hay[word] = int(val)
	for i in range(n):
		sal = 0
		line = input()
		while line != ".":
			for w in line.split():
				if w not in hay:
					continue
				sal += hay[w]
			line = input()
		print(sal)




if __name__ == "__main__":
	main()
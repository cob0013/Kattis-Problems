def main():
	firstNames = dict()
	names = []
	while True:
		try:
			first, last = input().split()
			names.append((last, first))
			if first not in firstNames:
				firstNames[first] = 1
			else:
				firstNames[first] += 1
		except:
			break

	names.sort()
	for name in names:
		if firstNames[name[1]] > 1:
			print(name[1], name[0])
		else:
			print(name[1])






if __name__ == '__main__':
	main()
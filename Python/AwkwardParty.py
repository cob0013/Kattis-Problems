def main():
	unique = set()
	n = int(input())
	line = input().split()
	for i in line:
		unique.add(int(i))
	print(n - (n - len(unique)))

if __name__ == '__main__':
	main()

	##not finished
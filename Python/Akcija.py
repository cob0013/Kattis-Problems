def main():
	n = int(input())
	books = []
	free = 0
	for i in range(n):
		books.append(int(input()))
	books.sort(reverse = True)
	for i in range(2, n, 3):
		free += books[i]

	print(sum(books) - free)




if __name__ == '__main__':
	main()

	# 6 5 5 5 5 4

def main():
	r, s, k = map(int, input().split())
	picture = []
	for i in range(r):
		picture.append(list(input()))
	maxflies = 0
	count = 0
	start = (0, 0)
	# selects everypoint racket can be placed at
	for i in range(r - k + 1):
		for j in range(s - k + 1):
			count = 0
			# checks flies in racket
			for l in range(1, k - 1):
				for m in range(1, k - 1):
					if picture[i + l][j + m] == "*":
						count += 1
					if count > maxflies:
						maxflies = count
						start = (i , j) 
	starti, startj = start
	picture[starti][startj] = "+"
	picture[starti + k - 1][startj + k - 1] = "+"
	picture[starti][startj + k - 1] = "+"
	picture[starti + k - 1][startj] = "+"
	for i in range(1, k - 1):
		picture[starti + i][startj] = "|"
		picture[starti + i][startj + k - 1] = "|"
		picture[starti][startj + i] = "-"
		picture[starti + k - 1][startj + i] = "-"
	print(maxflies)
	for line in picture:
		print(("".join(line)))


					

			


if __name__ == "__main__":
	main()
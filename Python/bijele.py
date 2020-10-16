def main():
	goal = [1, 1, 2, 2, 2, 8]
	output = []
	pieces = list(map(int, input().split()))
	for i in range(len(pieces)):
		output.append(goal[i] - pieces[i])
	print(" ".join(map(str, output)))

if __name__ == '__main__':
	main()
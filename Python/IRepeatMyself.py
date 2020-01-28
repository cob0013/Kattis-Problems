def main():
	n = int(input())
	for i in range(n):
		line = input()
		soFar = ''
		x = len(line)
		for j in range(len(line)):
			soFar += line[j]
			if (soFar * x)[:x] == line:
				print(len(soFar))
				break



			



if __name__ == '__main__':
	main()
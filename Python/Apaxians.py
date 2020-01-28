def main():
	line = list(input())
	output = line[0]
	
	for i in range(1, len(line)):
		if line[i] != line[i - 1]:
			output += line[i]


	print(output)
			
			
	


if __name__ == '__main__':
	main()
def main():
	alph = 'abcdefghijklmnopqrstuvwxyz'
	line = input()
	pointer = 0
	count = 0
	previous = 0
	for i in range(len(line)):
		if alph[pointer] == line[i] and previous < i:
			previous = i
			pointer += 1
			continue
		count += 1
	print(count)


# not finished



if __name__ == '__main__':
	main()
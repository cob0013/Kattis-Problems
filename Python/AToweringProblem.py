def main():
	tower1 = []
	tower2 = []
	line = list(map(int, input().split()))
	heights = line[:6]
	h1 = line[-2]
	h2 = line[-1]
	found = False

	for i in range(6):
		for j in range(i + 1, 6):
			for k in range(j + 1, 6):
				height = line[i] + line[j] + line[k]
				if height == h1:

					tower1.append(line[i])
					tower1.append(line[j])
					tower1.append(line[k])
					tower2 = (a for a in heights if a not in tower1)


					found = True
					break
				if height == h2:
					tower2.append(line[i])
					tower2.append(line[j])
					tower2.append(line[k])
					tower1 = (a for a in heights if a not in tower2)
					found = True
			if found:
				break
		if found:
			break




	tower1 = sorted(tower1, reverse = True)
	tower2 = sorted(tower2, reverse = True)
	output = ""
	for i in tower1:
		output += str(i) + " "
	for j in tower2:
		output += str(j) +" "
	print(output)
if __name__ == '__main__':
	main()
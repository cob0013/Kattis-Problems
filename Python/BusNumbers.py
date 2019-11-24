def main():
	n = int(input())
	stops = list(map(int, input().split()))
	output = []
	stops.sort()
	i = 0
	while i < n:
		count = 0
		for j in range(i + 1, n):
			if stops[j] - stops[j- 1] != 1:
				break
			else:
				count += 1
		if count >= 2:
			output.append(str(stops[i]) +'-' + str(stops[i + count]))
			i += count + 1
		else:
			output.append(str(stops[i]))
			i += 1
	print(" ".join(output))

	
		






				

if __name__ == '__main__':
	main()


##not finished
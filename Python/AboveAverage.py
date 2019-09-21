import statistics
n = int(input())
for i in range(n):
	line = list(map(float, input().split()))
	test = line[0]
	line = line[1:]
	average = statistics.mean(line)
	count = 0
	for x in line:
		if x > average:
			count += 1
	output = (count / test * 100)
	print(format(output, '.3f') + "%")
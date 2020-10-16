from itertools import permutations
def main():
	partitions = []
	w, p = map(int, input().split())
	partitions.append(w)
	partitions.append(0)
	widths = map(int, input().split())
	for i in widths:
		partitions.append(i)
	output = set()
	for i in range(len(partitions)):
		for j in range(i + 1, len(partitions)):
			if partitions[j] - partitions[i] != 0:
				output.add(abs(partitions[j] - partitions[i]))
	output = list(map(int, output))
	output.sort()
	output = list(map(str, output))

	print(" ".join(output))

if __name__ == '__main__':
	main()
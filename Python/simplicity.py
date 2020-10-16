def main():
	word = input()
	counts = set()
	for l in word:
		count = count = sum(map(lambda x : 1 if l in x else 0, word))
		counts.add((count, l))
	counts = list(counts)
	counts.sort(reverse = True)
	min = 0
	for i in range(2, len(counts)):
		min += counts[i][0]
	print(min)


		
if __name__ == "__main__":
	main()
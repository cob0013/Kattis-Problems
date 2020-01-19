


def main():
	total = 0
	for line in sys.stdin:
		if line == "\n":
			print()
			total = 0
		else:
			count = line.count("*")
			length = len(line) - 1
			total += count
			print(((length - total)  * ".") + (count * "*") + ("." * (total - count)))



	



if __name__ == "__main__":
	main()
def main():
	num = [0, 11]
	n = int(input())
	while n != 0:
		response = input()
		if response == "too high":
			num[1] = min(num[1], n)
		if response == "too low":
			num[0] = max(num[0], n)
		if response == "right on":
			if n < num[1] and n > num[0]:
				print("Stan may be honest")
			else:
				print("Stan is dishonest")
			num = [0, 11]
		n = int(input())

	
if __name__ == "__main__":
	main()

	# (1, 4) num = 5
	# (4, 7)

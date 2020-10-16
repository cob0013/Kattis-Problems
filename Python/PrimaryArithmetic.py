def main():
	a, b = map(int, input().split())
	while a != 0 or 0 != b:
		carried = 0
		count = 0
		while a != 0 or 0 != b:
			digit1 = a % 10
			digit2 = b % 10
			add = digit1 + digit2 + carried
			if add > 9:
				count += 1
				carried = 1
			else:
				carried = 0
			a //= 10
			b //= 10
		if count == 0:
			print("No carry operation.")
		elif count == 1:
			print("1 carry operation.")
		else:
			print(str(count)+ " carry operations.")

		a, b = map(int, input().split())


if __name__ == "__main__":
	main()
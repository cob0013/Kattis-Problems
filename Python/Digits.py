def main():
	number = input()
	while number != "END":
		count = 0
		curr = number
		nxt = str(len(number))
		if number == "1":
			print(1)
		else:
			while curr != nxt:
				count += 1
				temp = nxt
				curr = temp
				nxt = str(len(temp))
			print(count + 1)
		number = input()


			




if __name__ == "__main__":
	main()
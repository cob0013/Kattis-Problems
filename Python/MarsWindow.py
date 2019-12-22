def main():
	y = int(input())
	current = 3 + (2018 * 12)
	beggining = 12 * y
	end = 12* (y + 1)
	if y == 2018:
		print("yes")
	else:
		while current <= end:
			current += 26
			if beggining <= current and current < end:
				print("yes")
				break
		else:
			print("no")


if __name__ == "__main__":
	main()
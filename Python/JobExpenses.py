def main():
	n = int(input())
	prices = map(int, input().split())
	expense = 0
	for p in prices:
		if p < 0:

			expense += abs(p)

	print(expense)



if __name__ == "__main__":
	main()
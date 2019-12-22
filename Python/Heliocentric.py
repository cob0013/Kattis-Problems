def main():
	case = 1
	while True:
		try:
			days = 0
			e, m = map(int, input().split())
			while e % 365 != 0 or m % 687 != 0:
				days += 1
				e += 1
				m += 1

			print("Case " + str(case) + ": " + str(days))
			case += 1
			

		except:
			break

if __name__ == "__main__":
	main()
def main():
	k = int(input())
	for i in range(k):
		n = int(input())
		dvds = list(map(int, input().split()))
		lookingfor = 1
		moves = 0
		for dvd in dvds:
			if dvd != lookingfor:
				moves += 1
			else:
				lookingfor += 1
		print(moves)


if __name__ == "__main__":
	main()
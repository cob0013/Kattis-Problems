def oneDay(n):
	return n - 1

def main():
	n = int(input())
	trees = list(map(int, input().split()))
	trees.sort(reverse = True)
	planted = []
	days = 0
	planted.append(trees[0])
	for i in range(n):
		days += 1
		planted.append(trees[i])
	for i in range(n):
		planted[i] -= n - i
	planted.sort(reverse = True)
	while planted[0] > 0:
		planted[0] -= 1
		days += 1
	print(days + 1)


if __name__ == "__main__":
	main()
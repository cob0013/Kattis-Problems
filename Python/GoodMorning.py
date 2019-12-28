def works(n):
	dic = {1:(0, 0), 2:(0, 1), 3: (0, 2),
	4: (1, 0), 5: (1, 1), 6 : (1, 2), 7 : (2, 0),
	8 : (2, 1), 9 :(2, 2), 0 : (3, 1)}
	for i in range(1, len(n)):
		previous = int(n[i - 1])
		current = int(n[i])
		if dic[current][0] < dic[previous][0] or dic[current][1] < dic[previous][1]:
			return False
	return True

def main():
	n = int(input())
	for i in range(n):
		q = input()
		if works(q):
			print(q)
		else:
			i = 1
			while True:
				q1 = str(int(q) + i)
				q2 = str(int(q) - i)

				if works(q1):
					print(q1)
					break
				if works(q2):
					print(q2)
					break
				i += 1

if __name__ == "__main__":
	main()
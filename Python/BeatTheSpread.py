def main():
	n = int(input())
	for i in range(n):
		s, d = map(int, input().split())
		x = (s + d) // 2
		y = x  - d
		if 2 * x == s + d and y >= 0:
			print(max(x, y), min(x, y))
		else:
			print("impossible")








if __name__ == '__main__':
	main()




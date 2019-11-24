def main():
	while True:
		try:
			n = int(input())
			if n == 0:
				print(0)
			elif n == 1:
				print(1)
			else:
				print(n + (n - 2))
			

		except:
			break

if __name__ == '__main__':
	main()
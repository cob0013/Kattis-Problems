def main():
	while True:
		try:
			j = set()
			line = list(map(int, input().split()))
			n = line[0]
			if n == 1:
				print("Jolly")
				continue
			for i in range(1, n):
				diff = abs(line[i] - line[i + 1])
				if diff in j or diff > n - 1:
					print("Not Jolly")
					break
				j.add(diff)
			else:
				print("Jolly")
		except:
			break
		

if __name__ == "__main__":
	main()
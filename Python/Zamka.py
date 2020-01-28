def sum(n):
	sum = 0
	for digit in n:
		sum += int(digit)
	return sum

def main():
	l = int(input())
	d = int(input())
	x = int(input())
	output = []
	for i in range(l, d + 1):
		if sum(str(i)) == x:
			output.append(str(i))
			break
	for i in range(d, l - 1, -1):
		if sum(str(i)) == x:
			output.append(str(i))
			break
	print("\n".join((output)))

if __name__ == "__main__":
	main()
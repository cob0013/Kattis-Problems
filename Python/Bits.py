def countOnes(num):
	count = 0
	for n in num:
		if n == '1':
			count += 1
	return count

def main():

	n = int(input())
	for i in range(n):
		count = 0
		line = input()
		for i in range(len(line)):
			binary  = bin(int(line[0 : i + 1]))
			count =  max(countOnes(str(binary)), count)
		print(count)


			


if __name__ == '__main__':
	main()

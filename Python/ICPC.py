import math
def calc(n, type):
	
	if type == 1:
		# if fact is too big it will not finish under 7 seconds
		if n > 100000:
			return 1111111111111111111
		output = math.factorial(n)
	if type == 2:
		output = 2 ** n	
	if type == 3:
		output = n ** 4
	if type == 4:
		output = n ** 3
	if type == 5:
		output = n ** 2
	if type == 6:
		output = n *math.log(n, 2)
	if type == 7:
		output = n
	return output


def main():
	limit, n, t = map(int, input().split())
	if calc(n, t) > limit:
		print("TLE")
	else:
		print("AC")

if __name__ == '__main__':
	main()
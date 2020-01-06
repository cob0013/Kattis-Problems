import math
def price(k, p, a, b, c, d):
	return p * (math.sin(a * k + b) + math.cos(c * k + d) + 2)
def main():
	p, a, b, c, d, n = map(int, input().split())
	largestdecline = 0
	maxVal = price(1, p, a, b, c, d)
	for i in range(2, n + 1):
			if price(i, p, a, b, c, d) > maxVal:
				maxVal = price(i, p, a, b, c, d)
				
			elif largestdecline < maxVal - price(i, p, a, b, c, d):
				largestdecline = maxVal - price(i, p, a, b, c, d)
	print(largestdecline)
if __name__ == "__main__":
	main()
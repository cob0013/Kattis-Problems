import math
def maxArea(a, b, c, d):
	semiperimeter = (a + b + c + d) / 2

	return math.sqrt((semiperimeter - a) *
                    (semiperimeter - b) *
                    (semiperimeter - c) * 
                    (semiperimeter - d)) 
def main():
	a, b, c, d = map(int, input().split())
	print(maxArea(a, b, c, d))


if __name__ == "__main__":
	main()
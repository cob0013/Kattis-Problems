
def main():
	m, a, b, c, = map(int, input().split())
	if m * 2 >= a + b + c:
		print("possible")
	else:
		print("impossible")
	

if __name__ == "__main__":
	main()

#  6, 4
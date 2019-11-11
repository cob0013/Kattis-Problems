def main():
	steps = list(map(int, input().split()))
	steps.sort()
	print(steps[0] * steps[2])

if __name__ == "__main__":
	main()
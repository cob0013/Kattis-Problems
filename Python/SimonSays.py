def main():
	n = int(input())
	for i in range(n):
		command = input().split()
		if " ".join(command[:2]) == "Simon says":
			print(" ".join(command[2:]))


if __name__ == "__main__":
	main()
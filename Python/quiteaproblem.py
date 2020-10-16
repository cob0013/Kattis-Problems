def main():
	while True:
		try:
			line = input().lower()
			if "problem" in  line:
				print("yes")
			else:
				print("no")
		except:
			break


if __name__ == "__main__":
	main()
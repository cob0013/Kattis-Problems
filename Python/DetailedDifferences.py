def main():
	n = int(input())
	for i in range(n):
		s1 = input()
		s2 = input()
		output = []
		for i in range(len(s1)):
			if s1[i] == s2[i]:
				output.append('.')
			else:
				output.append('*')
		print(s1)
		print(s2)
		print("".join(output))
		print()
if __name__ == '__main__':
	main()
def main():
	k = int(input())
	yours = input()
	diff = 0
	same = 0
	friends = input()
	for i in range(len(yours)):
		if yours[i] == friends[i]:
			same += 1
	if same < len(yours) / 2:
		print(len(yours) - k)
	else:
		print(k + len(yours) - same)

if __name__ == "__main__":
	main()
# 6
# FTFTFTFTF
# TFFTFFTFF
# not finished
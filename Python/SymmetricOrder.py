def toString(d):
	print("\n".join(d))

import collections


def main():
	count = 1
	n = int(input())
	while n != 0:
		deq = collections.deque()
		names = []
		for i in range(n):
			names.append(input())
		for i in range(n - 1, -1, -1):
			if i % 2 == 0:
				deq.appendleft(names[i])
			else:
				deq.append(names[i])
		print("SET", count)
		toString(deq)
		n = int(input())
		count += 1



if __name__ == '__main__':
	main()
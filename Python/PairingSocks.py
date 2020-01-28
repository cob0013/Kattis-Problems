def main():
	n = 2 * int(input())

	socks = list(map(int, input().split()))
	aux = []
	count = 0
	while socks:
		if aux and socks[-1] == aux[-1]:
			count += 1
			socks.pop()
			aux.pop()
		else:
			aux.append(socks.pop())
	if len(aux) == 0:
		print(count * 2)
	else:
		print("impossible")




if __name__ == '__main__':
	main()
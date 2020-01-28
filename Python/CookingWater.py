def main():
	n = int(input())
	_range = [0, 1001]
	for i in range(n):
		start, end = map(int, input().split())
		_range[0] = max(start, _range[0])
		_range[1] = min(end, _range[1])
		if _range[0] > _range[1]:
			print("edward is right")
			break
	else:
		print("gunilla has a point")



if __name__ == '__main__':
	main()
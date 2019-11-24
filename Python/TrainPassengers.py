def main():
	c, n = map(int, input().split())
	on_board = 0
	waiting = 0
	consistent = True
	for i in range(n):
		left, entered, stay = map(int, input().split())
		if i == 0:
			if left != 0:
				consistent = False
				break
		waiting = stay
		on_board += entered
		on_board -= left
		if on_board  > c or on_board < 0:
			consistent = False
			break
		if on_board < c and waiting > 0:
			consistent = False
			break
	if on_board == 0 and consistent and waiting == 0:
		print("possible")
	else:
		print("impossible")



if __name__ == '__main__':
	main()
def main():
	# not finished
	house = 1
	while True:
		w, l = map(int, input().split())
		if w == 0 and l == 0:
			break
		room = []
		for i in range(l):
			room.append(input())
		for i in range(l):
			start = room[i].find("*")
			if start != -1:
				start = (i, start)
				break
		print(start)



		print(room)
if __name__ == "__main__":
	main()
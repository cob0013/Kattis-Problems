import math
def distance(p1, p2):
	return round(math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)))
def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		angle = math.radians(90)
		pos = [0, 0]
		for i in range(n):
			cmd, num = input().split()
			num = int(num)
			if cmd == "fd":
				pos[0] += num * math.cos(angle)
				pos[1] += num *math.sin(angle)
			if cmd == "lt":
				angle += math.radians(num)

			if cmd == "bk":
				pos[0] -= num * math.cos(angle)
				pos[1] -= num * math.sin(angle)
			if cmd == "rt":
				angle -= math.radians(num)
		print(distance((0, 0), pos))







if __name__ == "__main__":
	main()
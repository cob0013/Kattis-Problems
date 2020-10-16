import math
def distance(p0, p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
def main():
	d, n = input().split()
	while d != 0.0 and n != 0:
		d = float(d)
		n = int(n)
		countSour = 0
		countSweet = 0
		points = []
		for i in range(n):
			x, y = map(float, input().split())
			points.append([x, y])
		for i in range(n):
			flag = True
			for j in range(n):
				if i == j:
					continue
				if distance(points[j], points[i]) <= d:
					flag = False
			if flag:
				countSweet += 1
			else:
				countSour += 1
		d, n = input().split()
		d = float(d)
		n = int(n)
		output = str(countSour) + " sour, " + str(countSweet) +" sweet"
		print(output)
				
if __name__ == '__main__':
	main()

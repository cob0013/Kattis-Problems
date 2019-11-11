import math
def avg(l):
	x = 0
	y = 0
	for p in l:
		x += p[0]
		y += p[1]
	return str(x / len(l)) + " "  + str(y / len(l))
def distance(p0, p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
def furthest(points, start):
	worst = 0
	for p in points:
		if distance(p, start) > worst:
			worst = distance(p, start)
	return worst




def main():
	n = int(input())
	while n != 0:
		points = []
		for i in range(n):
			line = input().split()
			x = float(line[0])
			y = float(line[1])
			angle = float(line[3])
			point = [x , y]
			for j in range(5, len(line), 2):
				num = float(line[j])
				instructions = line[j - 1]
				if instructions == 'turn':
					angle += num
				else:
					point[0] += num * (math.cos(math.radians(angle)))
					point[1] += num * (math.sin(math.radians(angle)))
			points.append(point)
		
		output = str(avg(points)) + " " + str(furthest(points, list(map(float, avg(points).split()))))
		print(output)
		n = int(input())




if __name__ == '__main__':
	main()
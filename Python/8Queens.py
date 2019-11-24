def slope(p1, p2):
	return (p2[1] - p1[1]) / (p2[0] - p1[0])

def diag(points):
	for i in range(len(points)):
		p1 = points[i]
		for j in range(len(points)):
			if j == i:
				continue
			if (abs(slope(p1, points[j]))) == 1:
				return False
	return True

def horizontal(points):
	for i in range(len(points)):
		p1 = points[i]
		for j in range(len(points)):
			if j == i:
				continue
			if p1[0] == points[j][0]:
				return False
	return True

def vertical(points):
	for i in range(len(points)):
		p1 = points[i]
		for j in range(len(points)):
			if j == i:
				continue
			if p1[1] == points[j][1]:
				return False
	return True

def main():
	points = []
	for i in range(8):
		line = input()
		for j in range(8):
			if line[j] == '*':
				points.append((j, i))
	if (len(points) == 8 and vertical(points) and horizontal(points) and diag(points)):
		print('valid')
	else:
		print('invalid')

if __name__ == '__main__':
	main()
def main():
	n = int(input())
	while n != 0:
		verts = []
		direction = 0
		product1 = 0
		product2 = 0
		total = 0 
		for i in range(n):
			x, y = map(int, input().split())
			verts.append((x, y))
		for i in range(n - 1):
				direction += (verts[i + 1][0] - verts[i][0]) * (verts[i + 1][1] + verts[i][1])			
		verts.append((verts[0]))	
		for i in range(n):
			product1 = (verts[i][0] * verts[i + 1][1])
			product2 = (verts[i][1] * verts[i + 1][0])
			total += (product2 - product1)

		if total < 0:
			print("CCW", round(abs(total / 2), 1))
		else:
			print("CW", round(abs(total / 2), 1))
		n = int(input())




if __name__ == '__main__':
	main()
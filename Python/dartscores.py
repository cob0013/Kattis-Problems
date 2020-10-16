def main():
	goal = int(input())
	multiplier = ['single', 'double', 'triple']
	output = []
	score = 0
	found = False
	for i in range(20, 0,  -1):
		if found:
			break
		for j in range(20, 0,  -1):
			if found:
				break
			for k in range(20, 0,  -1):
				if found:
					break
				for l in range(3, -1, -1): 
					if found:
						break
					for m in range(3, -1, -1):
						if found:
							break
						for n in range(3, -1, -1):
							if (i * l) + (j * m )+ (k * n) == goal:
								if l != 0:
									print(multiplier[l -1 ], i)
								if m != 0:
									print(multiplier[m -1 ], j)
								if n != 0:
									print(multiplier[n -1 ], k)
								found = True
								break
	if not found:
		print("impossible")









if __name__ == '__main__':
	main()
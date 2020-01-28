def calc(n):
	signs = ['*', '+', '-', '//']
	exp = '4 {} 4 {} 4 {} 4'
	for i in range(4):
		for j in range(4):
			for k in range(4):
				if eval(exp.format(signs[i], signs[j], signs[k])) == n:
					return exp.format(signs[i], signs[j], signs[k]).replace("//" , "/") + "  = " + str(n)
	return "no solution"

def main():
	n = int(input())
	for i in range(n):
		print(calc(int(input())))



if __name__ == '__main__':
	main()
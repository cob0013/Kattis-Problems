import math

def main():
	r, b = map(int, input().split())
	tot = r + b
	found = False 
	for i in range(1, tot + 1):
		for j in range(int(tot / i) + 1):
			if i * j == tot and (i - 2)* (j - 2) == b:
				print(max(i, j), min(i, j))	
				found = True
				break	
		if found:
			break		

if __name__ == "__main__":
	main()
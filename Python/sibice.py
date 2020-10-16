import math
n, w, h = input().split()
n = int(n)
w = int(w)
h = int(h)
hyp = math.sqrt(w**2 + h**2)
for x in range(n):
	x = int(input())
	if x <= hyp:
		print("DA")
	else:
		print("NE")


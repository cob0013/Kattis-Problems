
from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
while n != m:
	a = [0] * 10000
	b = [0] * 10000
	
	for i in range(n):
		x, y, st, du = map(int, input().split())
		a[i] = st
		b[i] = st + du  - 1
	for i in range(m):
		ans = 0
		start, dur = map(int, stdin.readline().split())
		for j in range(n):
			if start  <= a[j] or start + dur - 1 <=  b[j]:
				ans = ans + 1
		print(ans)
	n, m = map(int, input().split())



t = int(input())
for i in range(t):
	blank = input()
	n = int(input())
	total = 0
	for j in range(n):
		total += int(input())
	if total % n == 0:
		print("YES")
	else:
		print("NO")
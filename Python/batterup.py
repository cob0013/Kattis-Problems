n = int(input())
s = map(int, input().split())
output = 0
for num in s:
	if num != -1:
		output += num
	else:
		n -= 1
print(output / n)
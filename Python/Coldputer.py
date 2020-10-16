a = int(input())
t = input().split()
count = 0;
for x in t:
	if int(x) < 0:
		count += 1

print(count)

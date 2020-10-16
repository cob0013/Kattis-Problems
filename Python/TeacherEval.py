line1 = input().split()
n = int(line1[0])
p = int(line1[1])
sum = 0
scores = input().split()
for i in scores:
	sum = sum + int(i)

avg = sum / n
count = 0
while avg < p:
	n = n + 1
	sum = sum + 100
	avg = sum / n
	count = count + 1
	if count > 100000:
		break

if count < 100000:
	print(count)
else:
	print("impossible")

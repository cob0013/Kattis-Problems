n, p, k = map(int, input().split())
times = input().split()
p = float(p / 100)
output = 0.0
count = 0
prev  = 0
diff = []
for i in times:
	diff.append(int(i) - prev)
	prev = int(i)
	
diff.append(k - int(times[-1]))

for t in diff:
	output += (count * p + 1) * t
	count += 1
print(output)


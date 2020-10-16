num = int(input())
rolls = list(map(int, input().split()))
count = {}
max = None
found = False
for i in rolls:
	if i in count:
		count[i] += 1
	else:
		count[i] = 1
for i in range(num):
	if not found and count[rolls[i]] == 1:
		max = i
		found = True
	elif count[rolls[i]] == 1 and rolls[i] > rolls[max]:
		max = i
if found:
	print(max + 1)
else:
	print("none")






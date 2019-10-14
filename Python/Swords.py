n = int(input())
TB = 0
LR = 0
count = 0
for i in range(n):
	line = input()
	TB -= int(line[0]) - 1
	TB -= int(line[1]) - 1
	LR -= int(line[2]) - 1
	LR -= int(line[3]) - 1


count = 0
while TB >= 2 and LR >= 2:
	TB -= 2
	LR -= 2
	count+= 1
print(str(count) + " " + str(TB) + " " + str(LR))

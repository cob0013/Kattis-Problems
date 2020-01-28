n = int(input())
for i in range(n):
	count = 0
	d = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
	streetName = input()
	addresses = input()
	m = int(addresses.split()[0])
	while count != m:
		line = input().split()
		if line[0] == "+":
			for i in range(int(line[1]), int(line[2]) + 1, int(line[3])):
				count += 1
				for digit in str(i):
					d[digit] += 1
		else:
			count += 1
			for digit in line[0]:
				d[digit] += 1

	print(streetName)
	print(addresses)
	total = 0
	for i in range(10):
		print("Make " + str(d[str(i)]) + " digit " + str(i))
		total += d[str(i)]
	if total > 1:
		print("In total " + str(total) + " digits")
	else:
		print("In total " + str(total) + " digit")





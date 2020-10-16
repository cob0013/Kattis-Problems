h,m = input().split()
h = int(h)
m = int(m)
if (m > 45 and m != 0):
	print(str(h) + " " + str((m-45)))
elif (h == 0):
	print(str(23) + " " + str(m + 15))
else:
	print(str(h -1) + " " + str(m +15))

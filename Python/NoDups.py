words = input().split()
output = "yes"
check = set()
for word in words:
	if word in check:
		output = "no"
		break
	else:
		check.add(word)
print(output)




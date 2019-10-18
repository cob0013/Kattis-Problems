def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
line = input()
test = ""
best = line
for i in range(1, len(line) - 1):
	for j in range(i + 1, len(line)):
		one = line[:i]
		two = line[i:j]
		three = line[j:]
		one = reverse(one)
		two = reverse(two)
		three = reverse(three)
		test = one + two + three
		if test < best:
			best = test
print(best)


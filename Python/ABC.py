nums = list(map(int, input().split()))
nums.sort()
output = ""
pairs = { "A" : nums[0], "B" : nums[1], "C" : nums[2]}
order = input()
for char in order:
	output += str(pairs[char]) + " "
print(output.strip())

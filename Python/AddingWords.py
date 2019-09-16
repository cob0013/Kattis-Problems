# https://open.kattis.com/problems/addingwords
import sys
words = {}
nums = {}
for l in sys.stdin:	
	line = l.split()
	if line[0] == "def":
		if line[1] in words:
			del nums[int(words[line[1]])]
		word = line[1]
		words[word] = int(line[2])
		nums[int(line[2])] = word
	elif line[0] == "calc":
		line = line[1:]
		function = line[::2]
		ops = line[1::2]
		unknown = False
		output = ""
		for val in function:
			if val not in words:
				unknown = True
		if not unknown:
			total = words[function[0]]
			for i in range(len(ops) - 1):
				if ops [i] == "+":
					total += words[function[i + 1]]
				if ops [i] == "-":
					total -= words[function[i + 1]]
			if total not in nums:
				unknown = True
		if unknown:
			output += "unknown"
		else:
			output += nums[total]
		print(" ".join (line), output)

	else:
		words = {}
		nums = {}









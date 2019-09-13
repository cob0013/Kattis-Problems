n = int(input())
previous = input()
count = 1
words = set()
words.add(previous)
for i in range(n):
	word = input()
	if  (word not in words) and (previous[len(previous) - 1] == word[0]):
		words.add(word)
		previous = word
		count += 1
		if (count == n):
			print ("Fair Game")
			break
	else:
		if i % 2 == 0:
			print("Player 2 lost")
			break
		else:
			print("Player 1 lost")
			break


	
def main():
	letters = ['A','B','C','D','E','F','G',
           'H','I','J','K','L','M','N',
           'O','P','Q','R','S','T','U',
           'V','W','X','Y','Z']
	line = input()
	firstHalf = line[0:len(line) // 2]
	firstHalfValue = 0
	secondHalf = line[len(line)// 2 ::]
	secondHalfValue = 0
	for i in range(len(firstHalf)):
		firstHalfValue += letters.index(firstHalf[i])
		secondHalfValue += letters.index(secondHalf[i])
	final = ''
	for i in range(len(firstHalf)):

		final.append(letters[(letters.index(firstHalf[i]) + firstHalfValue % 26 + letters.index(secondHalf[i]) + secondHalfValue % 26 % 26)])

	print(final)
	

if __name__ == '__main__':
	main()

##not finished
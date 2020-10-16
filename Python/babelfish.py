def main():
	dic = dict()
	while True:
		try:
			word, translation = input().split()
			dic[translation] = word
		except:
			break
	while True:
		try:
			w = input()
			if w in dic:
				print(dic[w])
			else:
				print("eh")

		except:
			break




if __name__ == '__main__':
	main()
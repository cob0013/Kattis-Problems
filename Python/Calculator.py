def main():
	while True:
		try:
			exp = input()
			print('{0:.2f}'.format(eval(((exp)))))
		except:
			break


if __name__ == '__main__':
	main()
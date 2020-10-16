def main():
	deck = set()
	count = {"P" : 13, "K" : 13, "H" : 13, "T" : 13}
	cards = input()
	for i in range(0, len(cards), 3):
		currentcard = cards[i: i + 3]
		if currentcard in deck:
			print("GRESKA")
			return
		deck.add(currentcard)
		count[currentcard[0]] -= 1

	print(count["P"],count["K"], count["H"], count["T"])

if __name__ == '__main__':
	main()
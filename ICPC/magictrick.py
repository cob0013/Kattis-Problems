def main():
    deck = input()
    print(1 if len(set(deck)) == len(deck) else 0)


if __name__ == "__main__":
    main()

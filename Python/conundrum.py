def main():
    word = input()
    PER = "PER" * len(word)
    count = 0
    for i in range(len(word)):
        if word[i] != PER[i]:
            count += 1
    print(count)

if __name__ == "__main__":
    main()

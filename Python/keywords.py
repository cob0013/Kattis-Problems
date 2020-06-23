def main():
    n = int(input())
    words = set()
    for i in range(n):
        s = input().lower()
        words.add(s.replace(" ", "-"))

    print(len(words))


if __name__ == "__main__":
    main()

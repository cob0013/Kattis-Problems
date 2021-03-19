def main():
    k = int(input())
    desks = []
    for i in range(k):
        desks.append(int(input()))
    count = 1
    for i in range(k - 1):
        if desks[i] > desks[i + 1]:
            count += 1
    print(count)

if __name__ == "__main__":
    main()

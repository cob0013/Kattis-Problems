def main():
    n = int(input())
    total = 0
    for i in range(1, n+ 1):
        line = input()
        num = int(line[:len(line)-1])
        p = int(line[-1])
        total += num ** p
    print(total)

if __name__ == "__main__":
    main()


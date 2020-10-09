def main():
    x = int(input())
    n = len(str(x))
    check = sorted(str(x))
    while len(str(x)) == n:
        x += 1
        if check == sorted(str(x)):
            print(x)
            return
    print(0)

if __name__ == "__main__":
    main()

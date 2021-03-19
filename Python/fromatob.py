def main():
    a, b = map(int, input().split())
    if a <= b:
        print(b - a)
        return
    count = 0
    while (a >= b):
        if a ^  1  == a + 1:
            a = a >> 1
        else:
            a = (a + 1)
        count += 1
    print(int(count + b - a))

if __name__ == "__main__":
    main()

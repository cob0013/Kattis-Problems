def main():
    c = float(input())
    l = int(input())
    total = 0
    for i in range(l):
        x, y = map(float, input().split())
        total += x * y * c
    print(total)
if __name__ == "__main__":
    main()

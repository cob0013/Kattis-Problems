def main():
    s, c, k = map(int, input().split())
    socks = [int(x) for x in input().split()]
    socks.sort()
    socks_in = 1
    previous = 0
    washers = 1
    current = 1
    while current < len(socks):
        if abs(socks[current] - socks[previous]) <= k and socks_in < c:
            socks_in += 1
        else:
            socks_in = 1
            previous = current
            washers += 1
        current  += 1
    print(washers)
if __name__ == "__main__":
    main()

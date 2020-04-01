def main():
    n, x = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()
    i = 1
    while i < len(prices):
            if prices[i] + prices[i - 1] > x:
                    break
            i += 1

    print(i)
if __name__ == "__main__":
        main()

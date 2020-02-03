def main():
    t = int(input())
    for i in range(t):
        stickers = dict()
        prizes = []
        n, m = map(int, input().split())
        for i in range(n):
            line = list(map(int, input().split()))
            prizes.append((line[-1], line[1:len(line) - 1))
        
        print(prizes)

if __name__ == "__main__":
    main()

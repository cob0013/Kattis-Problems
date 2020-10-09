def main():
    n, t = map(int, input().split())
    best = [0 for i in range(t)]
    for i in range(n):
        m, timeleft = map(int, input().split())
        for j in range(timeleft, -1, -1):
            if m > best[j]:
                best[j], m = m, best[j]
    print(sum(best))


if __name__ == "__main__":
    main()  

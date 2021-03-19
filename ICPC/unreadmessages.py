def main():
    n, m = map(int, input().split())
    unreads = dict()
    unreads_count = 0
    for i in range(m):
        sender = int(input())
        if sender - 1 not in unreads:
            unreads[sender - 1] = 0
        unreads_count = unreads_count + (n - 1) - (i - unreads[sender - 1])
        unreads[sender - 1] = i + 1
        print(unreads_count)
        


if __name__ == "__main__":
    main()

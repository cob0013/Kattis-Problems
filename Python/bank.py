def main():
    n, t = map(int, input().split())
    people = dict()
    for i in range(n):
        c, tleft = map(int, input().split())
        if tleft not in people:
            people[tleft] = []
        people[tleft].append(c)
    total = 0
    best = []
    for i in range(t)[::-1]:
        if i in people:
            for money in people[i]:
                best.append((-money))
        if best:
            best.sort()
            total += best.pop(0)
    print(abs(total))
if __name__ == "__main__":
    main()

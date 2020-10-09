def main():
    t = int(input())
    for i in range(t):
        p, r, f = map(int, input().split())
        print(sim(p, r, f))

def sim(p, r, f):
    i = 0
    while 1:
        if f - p < 0:
            return i
        p *= r
        i += 1


if __name__ == "__main__":
    main()

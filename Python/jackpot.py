def gcf(a, b):
    while b:
        a, b = b, a % b 
    return a


def main():
    n = int(input())
    for i in range(n):
        works = True
        w = int(input())
        periods = list(map(int, input().split()))
        lcm = 1
        for p in periods:
            lcm = (p * lcm) // gcf(p, lcm)
            if lcm > 1000000000:
                print("More than a billion.")
                works = False
                break
        if works:
            print(lcm)
if __name__ == "__main__":
    main()

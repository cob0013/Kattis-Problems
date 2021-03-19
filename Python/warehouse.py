def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        toys = dict()
        for i in range(n):
            toy, count = input().split()
            if toy not in toys:
                toys[toy] = 0
            toys[toy] += int(count)
        print(len(toys))
        final = []
        for key, value in toys.items():
            final.append((-value, key))
        final.sort()
        for n, t in final:
            print(t, -n)



if __name__ == "__main__":
    main()

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        results = [0 for i in range(n)]
        for j in range(n):
            results[j] += int(input())
        _max = max(results)
        if results.count(_max) > 1:
            print("no winner")
        else:
            if _max  >  sum(results) / 2:
                print("majority winner", results.index(_max) + 1)
            else:
                print("minority winner", results.index(_max) + 1)

if __name__ == "__main__":
    main()

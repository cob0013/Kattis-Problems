def main():
    n = int(input())
    helium = list(map(int, input().split()))
    helium.sort()
    out = 1
    for i in range(1, n + 1):
        if i < helium[i - 1]:
                print("impossible")
                return
        out = min(out, helium[i - 1] / i)
    print(out)
if __name__ == "__main__":
    main()

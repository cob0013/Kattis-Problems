def main():
    n, t = map(int, input().split())
    tasks = [int(i) for i in input().split()]
    total = 0
    for i in range(n):
        if total + tasks[i] <= t:
            total += tasks[i]
        else:
            print(i)
            return
    print(n) 
if __name__ == "__main__":
    main()

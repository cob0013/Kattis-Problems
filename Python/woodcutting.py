def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        times = []
        for j in range(n):
            customer = list(map(int, input().split()))
            customer_time = sum(customer[1::])
            times.append(customer_time)
        times.sort()
        so_far = times[0]
        total = times[0]
        for t in range(1, n):
            total += so_far + times[t]
            so_far += times[t]

        print(total / n)







if __name__ == '__main__':
    main()
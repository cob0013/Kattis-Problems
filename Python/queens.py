def main():
    n = int(input())
    queens = [list((map(int, input().split()))) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            u, v = queens[i], queens[j]
            if u[0] == v[0] or u[1] == v[1]:
                print("INCORRECT")
                return
            if abs(u[0] - v[0]) / abs(u[1] - v[1]) == 1:
                print("INCORRECT")
                return
    print("CORRECT")
if __name__ == "__main__":
    main()

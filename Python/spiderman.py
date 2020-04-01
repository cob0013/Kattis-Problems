
def main():
    n = int(input())
    INF = 10001
    for i in range(n):
        nDistances = int(input())
        distances = list(map(int, input().split()))
        dpDistance = [i for i in range(n)][10001 for i in range(101)]
        dpDirection = [i for i in range(n)][10001 for i in range(101)]

        for d in distances:
             


if __name__ == "__main__":
    main()

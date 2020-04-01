def main():
    n = int(input())
    knowAll = {i for i in range(1, n + 1)}
    e = int(input())
    for i in range(e):
        villagers = list(map(int, input().split()))
        villagers.pop(0)
        villagers = set(villagers)
        if 1 in villagers:
            knowAll = villagers & knowAll
        else:
            knowAll = villagers | knowAll
    for v in sorted(list(knowAll)):
        print(v)
if __name__ == "__main__":
    main()

def main():
    n, m = map(int, input().split())
    owes = []
    for i in range(n):
        owes.append(int(input()))
    disjoinSets = [i for i in range(n)]
    for i in range(m):
        x, y = map(int, input().split())
        union(x, y, disjoinSets)
    check = dict()
    for i in range(n):
        amount = owes[i]
        dj = find(i, disjoinSets)
        if dj not in check:
            check[dj] = 0
        check[dj] += amount
    for x in check.values():
        if x != 0:
            print("IMPOSSIBLE")
            return
    print("POSSIBLE")



def union(x, y, parents):
    parents[find(x, parents)] = find(y, parents)

def find(child, parents):
    if parents[child] == child:
        return child
    parents[child] = find(parents[child], parents)
    return parents[child]

if __name__ == "__main__":
    main()

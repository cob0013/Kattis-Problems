def find(x, parents):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]
def union(x, y, p):
    p[find(x, p)] = p[find(y, p)]


def kruskal(edges, n):
    edges.sort()
    mst = set()
    dj = [i for i in range(n)]
    for edge in edges:
        w, u, v = edge
        if find(u, dj) != find(v, dj):
            union(u, v, dj)
            mst.add((edge))
    return mst

def main():
    while 1:
        n, m = map(int, input().split())
        if n == 0:
            return
        edges = []
        for i in range(m):
            u, v, w = map(int, input().split())
            if u > v:
                u, v = v, u
            edges.append((w, u, v))
        mst = kruskal(edges,n)
        _sum = 0
        tree = []
        for e in mst:
            _sum += e[0]
            tree.append((e[1], e[2]))

        tree.sort()
        if len(tree) != n - 1:
            print("Impossible")
        else:
            print(_sum)
            for a, b in tree:
                print(a, b)
        






if __name__ == "__main__":
    main()

def find(x, parents):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def union(x, y, parents):
    parents[find(x, parents)] = parents[find(y, parents)]

def kruskal(edges, n):
    edges.sort(reverse = True)
    mst = set()
    djs = [i for i in range(n)]
    for edge in edges:
        w, u, v = edge
        if find(u, djs) != find(v, djs):
            union(u, v, djs)
            mst.add(edge)
    return mst

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v, w = map(int, input().split())
        if u > v:
            u, v = v, u
        edges.append((w, u, v))
    mst = kruskal(edges, n)
    output = []
    for i in range(m):
        if edges[i] not in mst:
            output.append(str(i))
    print(edges)
    print(mst)
    print(" ".join(output))


if __name__ == "__main__":
    main()

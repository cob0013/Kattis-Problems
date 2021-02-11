from sys import stdin, stdout
def union(x, y, parents):
    parents[find(x, parents)] = parents[find(y, parents)]

def find(x, parents):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def kruskal(graph, c):
    mst = set()
    graph.sort()
    V = c
    parents = [i for i in range(c)]
    e = 0
    i = 0
    for edge in graph:
        w, u, v = edge
        x = find(u, parents)
        y = find(v, parents)

        if x != y:
            e = e + 1
            mst.add((w, u, v))
            union(x, y, parents)
    return mst
        
def main():
    t = int(stdin.readline())
    for i in range(t):
        m, c = map(int, stdin.readline().split())
        edges = []
        for i in range(c * (c - 1) // 2):
            u, v, w = map(int, stdin.readline().split())
            edges.append((w, u, v))
        mst = kruskal(edges, c)
        mincost = 0
        for edge in mst:
            mincost += edge[0]
        if (m - mincost - c >= 0 and c - 1 == len(mst)):
            stdout.write("yes\n")
        else:
            stdout.write("no\n")




if __name__ == "__main__":
    main()

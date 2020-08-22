INF = 9999999
def union(x, y, parents):
    parents[find(x, parents)] = parents[find(y, parents)]

def find(x, parents):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def kruskal(graph, c):
    mincost = 0
    graph.sort()
    V = c
    parents = [i for i in range(c)]
    e = 0
    i = 0
    while e < V - 1:
        i = i + 1
        w, u, v = graph[i]
        x = find(u, parents)
        y = find(v, parents)

        if x != y:
            e = e + 1
            mincost += w
            union(x, y, parents)
    return mincost
        
def main():
    t = int(input())
    for i in range(t):
        m, c = map(int, input().split())
        edges = []
        for i in range(c * (c - 1) // 2):
            u, v, w = map(int, input().split())
            edges.append((w, u, v))
        mst = kruskal(edges, c)
        if (m - mst - c >= 0):
            print("yes")
        else:
            print("no")




if __name__ == "__main__":
    main()

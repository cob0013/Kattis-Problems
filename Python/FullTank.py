def main():
    n, m = map(int, input().split())
    gasPrices = map(int, input().split())
    graph = [dict() for i in range(n)]
    for i in range(m):
        u, v, d = map(int, input().split())
        graph[u][v] = d
        graph[v][u] = d
    
if __name__ == "__main__":
    main()

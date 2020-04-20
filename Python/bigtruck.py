import heapq
from sys import stdin

def main():
    n = int(stdin.readline())
    items = list(map(int , stdin.readline().split()))
    m = int(stdin.readline())
    graph = [[0 for i in range(n)] for i in range(n)]
    for i in range(m):
            u, v, d = map(int , stdin.readline().split())
            graph[u - 1][v - 1] = d
            graph[v - 1][u - 1] = d
    visited = set()
    pq = [(0, -items[0], 0)]
    
    found = False
    while pq:
            dist, count, curr = heapq.heappop(pq)
            if curr in visited:
                    continue
            if curr == n - 1:
                    found = True                            
                    print(dist, -count)
                    return
                    
            
            else:
                    visited.add(curr)
            for i in range(n):
 
                   if graph[curr][i] != 0 and i not in visited:
                           heapq.heappush(pq, (dist + graph[curr][i], count - items[i], i))
                               
    
    print("impossible")

if __name__ ==  "__main__":
        main()

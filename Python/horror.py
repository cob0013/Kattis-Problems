from collections import deque
def main():
    n, h, l = map(int, input().split())
    horror_list = list(map(int, input().split()))
    graph = dict()
    for i in range(n):
        graph[i] = [] 
    for i in range(l):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    q = deque()
    visited = set()
    for movie in horror_list:
        q.append((movie, 0))
        visited.add(movie)
    best_hi = -1
    best_m = -1
    while q:
        curr_movie, curr_count = q.popleft()
        if curr_count > best_hi or  (curr_count == best_hi and curr_movie < best_m):
            best_hi, best_m = curr_count, curr_movie
        for movie in graph[curr_movie]:
            if movie not in visited:
                visited.add(movie)
                q.append((movie, curr_count + 1))
    for i in range(n):
        if i not in visited:
            best_m  = i
            break
    print(best_m)
if __name__ == "__main__":
    main()

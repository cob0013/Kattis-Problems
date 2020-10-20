from collections import deque
def main():
    n, m, d = map(int, input().split())
    graph = dict()
    people  = dict()
    for i in range(n):
        name, npeople = input().split()
        graph[name] = []
        people[name] = int(npeople)
    for i in range(m):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)
    q = deque()
    start = input()
    q.append(start)
    visited = set()
    visited.add(start)
    for i in range(d):
        nextQ = []
        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                people[neighbor] -= 1
                if people[neighbor] == 0:
                   nextQ.append(neighbor)
        q = deque(nextQ)
    visited.remove(start)
    print(len(visited))

if __name__ == "__main__":
    main()

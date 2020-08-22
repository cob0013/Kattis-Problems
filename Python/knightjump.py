from collections import deque
def main():
    n = int(input())
    board = []
    for i in range(n):
        row = input()
        c = row.find("K")
        if c != -1:
            startr = i
            startc = c
        board.append(row)
    q = deque()
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2),
            (-1, 2), (-1, 2), (-1, -2)]
    q.append((startr, startc, 0))
    visited = set()
    visited.add((startr, startc))
    while q:
        currR, currC, count = q.popleft()
        if currR == 0 and currC == 0:
            print(count)
            return
        for x, y in moves:
            nextR = currR + x
            nextC = currC + y
            if nextR >= 0 and nextC >= 0 and nextC < n\
            and nextR < n and (nextR, nextC) not in visited and board[nextR][nextC] != "#":
                visited.add((nextR, nextC))
                q.append((nextR, nextC, count + 1))
    print(-1)

if __name__ == "__main__":
    main()

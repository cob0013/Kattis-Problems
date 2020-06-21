
from collections import deque
neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(grid, goalX, goalY):
    q = deque()
    visited = set()
    visited.add((0, 0))
    q.appendleft((0, 0, 0))
    while q:
        currX, currY, moves = q.pop()
        if currX == goalX and currY == goalY:
            return moves
        for i in grid[currX][currY]:
            dx, dy = neighbors[i]
            newx = currX + dx
            newy = currY + dy
            if (newx, newy) not in visited:
                visited.add((newx, newy))
                q.appendleft((newx, newy, moves + 1))
    return -1

def main():

    t = int(input())
    for i in range(t):
        input() 
        n = int(input())
        grid = dict()
        for i in range(-n, n):
            grid[i] = dict()
            for j in range(-n, n):
                grid[i][j] = []
        X = 0
        Y = 0
        for i in range(n):
            direction = input()
            if direction == "N":
                grid[X][Y].append(0)
                Y += 1
                grid[X][Y].append(1)
            if direction == "S":
                grid[X][Y].append(1)
                Y -= 1
                grid[X][Y].append(0)
            if direction == "E":
                grid[X][Y].append(2)
                X += 1
                grid[X][Y].append(3)
            if direction == "W":
                grid[X][Y].append(3)
                X -= 1
                grid[X][Y].append(2)
        print(bfs(grid, X, Y))
            

        

if __name__ == "__main__":
    main()

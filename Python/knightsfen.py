from collections import deque
GOAL = (('1', '1', '1', '1', '1'), ('0', '1', '1', '1', '1'),
       ('0','0', ' ', '1', '1,'), ('0', '0', '0', '0', '1'), ('0', '0', '0', '0', '0'))

#unfinished do dfs backwards from goal keep dict of move cound
def main():
    n = int(input())
    
    for i in range(n):
        board = []
        for i in range(5):
            board.append(list(input()))
        print(GOAL)
        print(board)

def dfs(board):
    visited = set()
    visited.add(board)
    check = {}
    check[board] = 0
    stack = deque()
    stack.append(board)
    while stack:
        curr = stack.pop()
        for i in range(5):
            for j in range(5):
                if curr[i][j] == " ":
                    start = (i, j)
                    break

def neighbors(board, i, j):
    X = [2, 1, -1, -2, -2, -1, 1, 2]; 
    Y = [1, 2, 2, 1, -1, -2, -2, -1]; 
    neigbs = ()
    for i in range(8):
        x = i + X[i]
        y = q + Y[i]
        if (x >= 0 and y >= 0 and x < 5 and y < 5):
            board[i][j] = board[x][y]
            board[x][y] = " "
            neigbs.append(toTuple(board))
    return neigbs

def toTuple(board):
    return tuple(map(tuple, board))
if __name__ == "__main__":
    main()

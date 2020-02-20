from collections import deque
from sys import stdin, stdout  

def main():
    while True:
        try:
            neighbors = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (-2, 1), (2, -1)]
            r, c, gr, gc, lr, lc = map(int, stdin.readline().split())
            q = deque()
            found = False
            q.append((gr, gc, 0))
            visited = set()
            visited.add((gr, gc))
            while q:
                currr, currc, moves = q.popleft()
               
                if currr == lr and currc == lc:
                    print(moves)
                    found = True
                    break
                for deltar, deltac in neighbors:
                	nextr = currr + deltar
                	nextc = currc + deltac
                	if (nextr, nextc) not in visited and inBounds(nextr, nextc, r, c):
                		visited.add((nextr, nextc))
                		q.append((nextr, nextc, moves + 1))
            if not found:
            	print("impossible")
        except:
            break

        
    


def inBounds(i, j, r, c):
    return i < r and j < c and i >= 0 and j >= 0
if __name__ == "__main__":
    main()

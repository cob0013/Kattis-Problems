from collections import deque 

def main():
    c, r = map(int, input().split())
    garden = []
    total = 0
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    for i in range(r):
        garden.append(list(map(int, input().split())))
    for i in range(r):
        for j in range(c):
            if (i, j) in visited:
                continue
            q = deque()
            count = 0
            floods = True
            q.append((i, j))
            visited.add((i, j))
            while q:
                currr, currc = q.popleft()
                count += 1 
                for mover, movec in  neighbors:
                    nextr = currr + mover
                    nextc = movec + currc
                    if (inBounds(nextr, nextc, r, c) and (nextr, nextc) not in visited
                    and garden[nextr][nextc] == garden[currr][currc]):
                        visited.add((nextr, nextc))
                        q.append((nextr, nextc))
                    if inBounds(nextr, nextc, r, c) and garden[currr][currc] > garden[nextr][nextc]:
                        floods = False
            if floods:
                total += count
    print(total)
           
def inBounds(r, c, rMax, cMax):
    return r >= 0 and c >= 0 and r < rMax and c < cMax
    
    print(garden)


if __name__ == "__main__":
    main()

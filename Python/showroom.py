import heapq
import sys
def main():
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    R, C = map(int, sys.stdin.readline().split())
    showroom  = []
    for i in range(R):
        showroom.append(sys.stdin.readline())
    startR, startC = map(int, sys.stdin.readline().split())
    pq = [(0, startR - 1, startC - 1)]
    visited = set()
    while pq:
        count, currR, currC = heapq.heappop(pq)
        if (currR, currC) in visited:
            continue
        visited.add((currR, currC))
        if showroom[currR][currC] == "D" and (currR == 0 or currC == 0
            or currR == R - 1 or currC == C - 1):
            print(count)
            return
        if showroom[currR][currC] == "c":
            count += 1

        for deltaR, deltaC in neighbors:
            nextR = deltaR + currR
            nextC = deltaC + currC
            if  inBounds(nextR, nextC, R, C) and showroom[nextR][nextC] != "#" and (nextR, nextC) not in visited:
                heapq.heappush(pq, (count, nextR, nextC))




def inBounds(r, c, R, C):
    return r >= 0 and c >= 0 and r < R and c < C
if __name__ == "__main__":
    main()

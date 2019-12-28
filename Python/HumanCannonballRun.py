# 5 m/s, 50 meter shot, 
# cant figure out why this is wrong
import math
import heapq
def dist(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def gettime(p1, p2, points):
    distance = dist(points[p1], points[p2])
    if p1 == 0:
        return distance / 5
    else:
        return 2 + abs(distance - 50) / 5
def main():
    startx, starty = map(float, input().split())
    goalx, goaly = map(float, input().split())
    if startx == goalx and starty == goaly:
        print(0)
        return
    n = int(input())
    points = [None] * (n + 2)
    points[0] = (startx, starty)
    points[1] = (goalx, goaly)
    pq = [(0, 0)]
    for i in range(2, n + 2):
        x, y = map(float, input().split())
        points[i] = (x, y)
    visited = set()
    while pq:
        time, point = heapq.heappop(pq)
        if point == 1:
            print(time)
            return
        if point in visited:
            continue
        visited.add(point)
        for i in range(n + 2):
            if i != point and i not in visited:
                heapq.heappush(pq, (time + gettime(point, i, points), i))







if __name__ == "__main__":
    main()
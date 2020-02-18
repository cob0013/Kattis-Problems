import math
from queue import PriorityQueue


def distance(p1, p2):
    return math.sqrt(((p1[1] - p2[1])**2) + ((p1[2] - p2[2])**2))


def gettime(p1, p2):
    dist = distance(p1, p2)
    if p1[0] != -1 and p1[0] == p1[0]:
        return dist / 40
    else:
        return dist / 10
    
def main():
    xhome, yhome, xschool, yschool = map(float, input().split())
    points = []
    points.append((-1, xhome, yhome))
    points.append((-1, xschool, yschool))
    count = 0
    while True:
        try:
            subway = list(map(float, input().split()))
            for i in range(0, len(subway) - 2, 2):
                x, y = subway[i : i + 2]
                points.append((count, x, y))
            count += 1
        except:
            break
    # dijkstras
    pq = PriorityQueue()
    pq.put((0, 0))
    visited = set()
    visited.add(0)
    while pq:
        print("here")
        time, point = pq.get()
        if point == 1:
            print(time)
            return
        if point in visited:
            continue
        visited.add(point)
        for i in range(2, len(points)):
            if i != point and i not in visited:
                heapq.heappush(pq, (time + gettime(points[point], points[i]), i))



     
if __name__ == "__main__":
    main()

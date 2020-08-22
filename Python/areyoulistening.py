import math
def main():
    cx, cy, n = map(int, input().split())
    distances = []
    for i in range(n):
        x, y, r = map(int, input().split())
        distances.append(math.hypot(cx - x, cy - y) - r)

    distances.sort()
    if distances[2] <= 0:
        print(0)
    else:
        print(math.floor(distances[2]))

if __name__ == "__main__":
    main()

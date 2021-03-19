def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    max_speed = -1
    for i in range(n - 1):
        speed = (points[i + 1][1] - points[i][1]) // (points[i + 1][0] - points[i][0])
        max_speed = max(max_speed, speed)
    print(max_speed)
            
            


if __name__ == "__main__":
    main()

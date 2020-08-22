#greedy
import math
def main():
    n, m, k = map(int, input().split())
    plots = sorted(map(int, input().split()), reverse = True)
    circle = list(map(int, input().split()))
    square = [int(i) * math.sqrt(2) / 2 for i in input().split()]
    houses = sorted(circle + square, reverse = True)
    count = 0
    for house in houses:
        if count == n:
            break
        if house < plots[count]:
            count += 1
    print(count)
if __name__ == "__main__":
    main()

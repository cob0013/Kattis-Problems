def main():
    n = int(input())
    for x in range(n):
        heights = list(map(int, input().split()))[1:]
        count = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                    if heights[i] > heights[j]:
                        count += 1
        print(x + 1, count)

if __name__ == "__main__":
    main()

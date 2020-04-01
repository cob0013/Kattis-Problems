def main():
    output = 0
    n = int(input())
    grid = []
    for i in range(n):
            grid.append(list(input()))
    for i in range(n):
            for j in range(n):
                    nearest = 99999999
                    if grid[i][j] == "S":
                            for k in range(n):
                                    for l in range(n):
                                            if grid[k][l] == "H":
                                                    nearest = min(nearest, abs(i - k) + abs(l - j))
                            output = max(output, nearest)
    print(output)
if __name__ == "__main__":
        main()

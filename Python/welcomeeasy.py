def solve(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(n + 1):
        dp[0][i] = 0
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]
def main():
    n = int(input())
    for i in range(n):
        line = input()
        ans = solve(line, "welcome to code jam")
        print("Case #{case}: {out}".format(case = i + 1, out = str(ans).zfill(4)[-4::]))


    
if __name__ == "__main__":
    main()

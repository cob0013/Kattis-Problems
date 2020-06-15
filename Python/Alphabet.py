def lis(s):
    n = len(s)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if ord(s[i]) > ord(s[j]) and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    m = 0
    for i in range(n):
        m = max(m, dp[i])
    return m

def main():
    line = input()
    print(26 - lis(line))


# not finished



if __name__ == '__main__':
	main()

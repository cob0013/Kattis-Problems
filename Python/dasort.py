import sys
def main():
    p = int(input())
    for i in range(p):
        k, n = map(int, sys.stdin.readline().split())
        data = []
        while n > 0:
            data.extend([int(i) for i in sys.stdin.readline().split()])
            n -= 10
        sys.stdout.write(str(k) + " " +  str(check(data)) + "\n")

def check(arr):
    corr = sorted(arr)
    right = 0
    for i in range(len(corr)):
        if corr[right] == arr[i]:
            right += 1
    return (len(arr) - right)


if __name__ == "__main__":
    main()

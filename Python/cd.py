from sys import stdin
def main():
    n, m = map(int, stdin.readline().split())
    
    while 1:
        if n == 0 and m == 0:
            return
        jacks = set()
        jills = set()
        for i in range(n):
            jacks.add(stdin.readline().strip())
        count = 0
        for i in range(m):
            if stdin.readline().strip() in jacks:
                count += 1
        print(count)
        
        n, m = map(int, stdin.readline().split())

if __name__ == "__main__":
    main()

import sys
def main():
    n, m  = map(int, sys.stdin.readline().split())
    sizes = []
    needed = []
    for i in range(n):
        sizes.append(int(sys.stdin.readline()))
    for i in range(m):
        needed.append(int(sys.stdin.readline()))
    sizes.sort()
    needed.sort()
    i = 0
    wasted = 0
    for color in needed:
        while i < len(sizes) and sizes[i] < color:
            i += 1
        wasted += sizes[i] - color
    print(wasted)
if __name__ == "__main__":
    main()

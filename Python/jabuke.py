def area(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0] * (a[1] - b[1]))) / 2

def main():
    a  = tuple(map(int, input().split()))
    b  = tuple(map(int, input().split()))  
    c  = tuple(map(int, input().split())) 
    areaOriginal =  (area(a, b, c))
    trees = int(input())
    count = 0
    for i in range(trees):
        tree = tuple(map(int, input().split()))
        a1 = area(tree, b, c)
        a2 = area(a, tree, c)
        a3 = area(a, b, tree)
        if areaOriginal == a1+ a2 + a3:
            count += 1
    print("{:.1f}".format(areaOriginal))
    print(count)
if __name__ == "__main__":
    main()

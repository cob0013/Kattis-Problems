def union(x, y, parents):
    parents[find(y, parents)] = find(x, parents)

def find(x, parents):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x], parents)
        return parents[x]
def main():
    p, t = map(int, input().split())
    parents = [i for i in range(t)]
    
    while True:
        try:    
           i, j = map(int, input().split())
           union(i-1, j-1, parents)
        except:
            break

    diff = set()
    for p in parents:
        diff.add(find(p, parents))


    print(len(diff))



if __name__ == "__main__":
    main()

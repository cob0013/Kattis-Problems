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
    opinions = [set() for i in range(p)] 
    while True:
        try:    
            i, j = map(int, input().split())
            opinions[i - 1].add(j)
        except:
            break
    diff = set()
    for o in opinions:
        diff.add(frozenset(o))
    print(len(diff))



if __name__ == "__main__":
    main()

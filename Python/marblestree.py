#unfinished


def main():
    n = int(input())
    tree = {i : set() for i in range(1, n + 1)} 
    marblesLeft = {i : 0 for i in range(1, n + 1)}

    for i in range(n):
        vertex = list(map(int, input().split()))
        v = vertex.pop(0)
        marbels = vertex.pop(0)
        marblesLeft[v] = marbels
        children = vertex.pop(0)
        for child in vertex:
            tree[v].add(child)
    print(tree)

if __name__ == "__main__":
    main()

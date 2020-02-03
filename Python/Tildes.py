from sys import stdin, stdout  

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.sizes = [1 for i in range(n)]
        self.unions = [i for i in range(n)]
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            self.sizes[parentY] += self.sizes[parentX]
            self.sizes[parentX] = self.sizes[parentY]
        self.unions[parentY] = parentX
    def find(self, x):
        if self.unions[x] == x:
            return x
        self.unions[x] = self.find(self.unions[x])
        return self.unions[x]


def main():
    n, q = map(int, stdin.readline().split())
    uf = UnionFind(n)
    parents = [i for i in range(n)]
    size = [1 for i in range(n)]
    for i in range(q):
        line = stdin.readline().split()
        if line[0] == "t":
            x = int(line[1]) - 1
            y = int(line[2]) - 1
            uf.union(x, y)
        else:
            x = int(line[1]) - 1
            stdout.write(str(uf.sizes[uf.find(x)])+ "\n")





if __name__ == "__main__":
    main()

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
    h, r, c = map(int, input().split())
    c *= 2
    uf = UnionFind(r * c)
    neigbhors = [(0, 2), (1, 1), (-1, 1)]
    if h == 0:
        print(0)
        return
    


    hive = []
    for i in range(r):
        # formatting
        space = ""
        if i % 2 == 0:
            space = " "
        hive.append(input() + space)
    for i in range(r):
        for j in range(c):
            if hive[i][j] == ".":
                for deltai, deltaj in neigbhors:
                    nexti = i + deltai
                    nextj = j + deltaj
                    if inBounds(nexti, nextj, r, c) and hive[nexti][nextj] == ".":
                        uf.union(i * c + j, nexti * c + nextj)

                
    openCells = set()
    for i in range(r):
        for j in range(c):
            if hive[i][j] == ".":
                x = uf.find(i * c + j)
                openCells.add((uf.sizes[x], x))
    openCells = list(openCells)
    openCells.sort(reverse = True)
    count = 0
    for size, djs in openCells:
        h -= size
        count += 1
        if h <= 0:
            break

    print(count)
                

def inBounds(i, j, r, c):
    return i < r and j < c and i >= 0 and j >= 0

if __name__ == "__main__":
    main()


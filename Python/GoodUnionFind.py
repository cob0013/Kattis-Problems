# not a kattis problem
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
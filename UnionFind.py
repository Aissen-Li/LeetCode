class UnionFind:
    def __init__(self, n):
        self.set = list(range(1, n+1))
    def find(self, x):
        if self.set[x] != x:
            self.set[x] = self.find(self.set[x])
        return self.set[x]
    def union(self, x, y):
        self.set[self.find(x)] = self.find(y)

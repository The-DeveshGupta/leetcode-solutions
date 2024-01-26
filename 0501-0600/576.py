class Solution:
    def __init__(self):
        self.m = None
        self.n = None
        self.dp = None

    def parseField(self, move, i, j):
        if 0 > i or i >= self.m or 0 > j or j >= self.n:
            return 1
        if 0 >= move:
            return 0
        if self.dp[move][i][j] is not None:
            return self.dp[move][i][j]

        paths = (self.parseField(move - 1, i, j - 1) + self.parseField(move - 1, i, j + 1)
                 + self.parseField(move - 1, i - 1, j) + self.parseField(move - 1, i + 1, j)) % 1000000007

        self.dp[move][i][j] = paths
        return paths

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.m = m
        self.n = n
        self.dp = [[[None for j in range(n)] for i in range(m)] for h in range(maxMove + 1)]
        return self.parseField(maxMove, startRow, startColumn)

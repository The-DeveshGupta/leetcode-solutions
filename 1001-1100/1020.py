class Solution:
    def numEnclaves(self, grid) -> int:

        n = len(grid)
        m = len(grid[0])
        output = 0

        def dfs(i, j):

            nonlocal flag
            if i < 0 or j < 0 or i >= n or j >= m:
                flag = 0
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)

            return left + right + up + down + 1

        for i in range(n):
            for j in range(m):
                flag = 1
                if grid[i][j]:
                    count = dfs(i, j)
                    if flag:
                        output += count

        return output

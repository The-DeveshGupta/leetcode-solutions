class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        max_row, max_col = len(grid), len(grid[0])

        @cache
        def parse_grid(r1_x, r2_x, row):
            if 0 <= r1_x < max_col and 0 <= r2_x < max_col and row < max_row and r1_x != r2_x:
                cherry = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        cherry = max(cherry, parse_grid(r1_x + i, r2_x + j, row + 1))

                return cherry + grid[row][r1_x] + grid[row][r2_x]
            else:
                return 0

        return parse_grid(0, max_col - 1, 0)

class Solution:
    def numSquares(self, n: int) -> int:

        @cache
        def break_num(n):
            count = float("inf")
            for i in range(int(n ** 0.5), 0, -1):
                if i * i == n:
                    return 1
                count = min(count, break_num(n - i * i) + 1)
            return count

        return break_num(n)

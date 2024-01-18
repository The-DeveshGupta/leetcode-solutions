class Solution:
    def factorial(x):
        if x > 1:
            return x * factorial(x - 1)
        else:
            return 1

    def climbStairs(self, n: int) -> int:
        ways = 0
        i = 0
        while n >= 0:
            ways += factorial(n + i) // (factorial(i) * factorial(n))
            i += 1
            n -= 2

        return ways

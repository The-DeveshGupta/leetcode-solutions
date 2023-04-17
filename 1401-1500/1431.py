class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        threshold = max(candies) - extraCandies
        return [threshold <= candy for candy in candies]

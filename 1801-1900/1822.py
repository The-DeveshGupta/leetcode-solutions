class Solution:
    def arraySign(self, nums: List[int]) -> int:
        positive = 1
        for num in nums:
            if num < 0:
                positive = -positive
            elif num == 0:
                return 0
        return positive

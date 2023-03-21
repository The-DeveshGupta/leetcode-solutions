class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        output = 0
        zero_count = 0
        for num in nums:
            if num:
                zero_count = 0
            else:
                zero_count += 1
                output += zero_count
        return output

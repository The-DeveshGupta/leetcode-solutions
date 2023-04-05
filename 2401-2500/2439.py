class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        n = len(nums)
        sum_ = sum(nums)

        for idx in range(n - 1, 0, -1):
            if n * nums[idx] > sum_:
                nums[idx - 1] = nums[idx - 1] + (n * nums[idx] - sum_) // n
                nums[idx] = nums[idx] - (n * nums[idx] - sum_) // n
            sum_ = sum_ - nums[idx]
            n -= 1

        return max(nums)

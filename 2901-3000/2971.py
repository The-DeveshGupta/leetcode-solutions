class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        csum = [0]

        for num in nums:
            csum.append(csum[-1] + num)

        for idx in range(len(nums) - 1, -1, -1):
            if idx < 2:
                pass
            elif nums[idx] < csum[idx]:
                return csum[idx + 1]

        return -1

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end)//2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                end = mid
            else:
                start = mid + 2
        return nums[start]

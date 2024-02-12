class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        _dict = defaultdict(int)
        limit = len(nums) // 2

        for num in nums:
            _dict[num] += 1
            if _dict[num] > limit:
                return num

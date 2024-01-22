class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        _list = [False] * len(nums)
        extra = None

        for num in nums:
            if _list[num - 1]:
                extra = num
            else:
                _list[num - 1] = True

        for idx, flag in enumerate(_list):
            if not flag:
                return extra, idx + 1

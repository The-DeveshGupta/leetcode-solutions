class Solution:
    def lengthOfLIS(self, nums) -> int:
        _list = [nums[0]]

        for num in nums[1:]:

            if num > _list[-1]:
                _list.append(num)
            else:
                idx = bisect.bisect_left(_list, num)
                _list[idx] = num

        return len(_list)

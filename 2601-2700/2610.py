class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums) + 1)
        output = []

        for num in nums:
            if freq[num] >= len(output):
                output.append([])
            output[freq[num]].append(num)
            freq[num] += 1

        return output

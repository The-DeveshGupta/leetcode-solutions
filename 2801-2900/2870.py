class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        total_operations = 0
        operation = lambda num: (num + 2) // 3
        for value in counter.values():
            if value == 1:
                return -1
            total_operations += operation(value)

        return total_operations

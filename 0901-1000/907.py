class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        size = len(arr)
        output = 0

        def get_arr(idx):
            if 0 <= idx < size:
                return arr[idx]
            else:
                return float("-inf")

        stack = [-1]

        for idx in range(size + 1):
            while stack and get_arr(idx) < get_arr(stack[-1]):
                last_idx = stack.pop()
                output = (output + get_arr(last_idx) * (idx - last_idx) * (last_idx - stack[-1])) % 1000000007
            else:
                stack.append(idx)

        return output

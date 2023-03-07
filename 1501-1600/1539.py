class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        if arr[0] > k:
            return k

        if (arr[-1] - len(arr)) < k:
            return k + len(arr)

        left, right = 0, len(arr)-1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k

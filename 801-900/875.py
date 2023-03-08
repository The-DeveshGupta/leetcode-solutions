class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        k_left = 1
        k_right = max(piles) // (h // len(piles)) + 1

        while k_left < k_right:
            k_mid = (k_left + k_right) // 2
            if sum((pile + k_mid - 1) // k_mid for pile in piles) > h:
                k_left = k_mid + 1
            else:
                k_right = k_mid

        return k_left

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_pot = 1
        for flower in flowerbed:
            if flower:
                n -= (empty_pot - 1) // 2 if empty_pot else 0
                empty_pot = 0
            else:
                empty_pot += 1
        else:
            n -= empty_pot // 2
        return n <= 0

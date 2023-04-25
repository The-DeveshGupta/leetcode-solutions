class SmallestInfiniteSet:

    def __init__(self):
        self.not_in_set = []

    def popSmallest(self) -> int:
        left = 0
        right = len(self.not_in_set)
        while left < right:
            mid = left + (right - left) // 2
            if self.not_in_set[mid] == (mid + 1):
                left = mid + 1
            else:
                right = mid
        self.not_in_set.insert(left, left + 1)
        return left + 1

    def addBack(self, num: int) -> None:
        if num in self.not_in_set:
            self.not_in_set.remove(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        _dict = defaultdict(int)

        for num in arr:
            _dict[num] += 1

        freqs = sorted(_dict.values())

        for idx, freq in enumerate(freqs):
            k = k - freq
            if k == 0:
                return len(freqs) - idx - 1
            elif k < 0:
                return len(freqs) - idx

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        _dict = defaultdict(int)

        for num in arr:
            _dict[num] += 1

        return len(set(_dict.values())) == len(_dict.values())

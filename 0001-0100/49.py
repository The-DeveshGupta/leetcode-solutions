class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)

        for s in strs:
            _dict["".join(sorted(s))].append(s)

        return _dict.values()

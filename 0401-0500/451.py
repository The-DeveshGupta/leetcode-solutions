class Solution:
    def frequencySort(self, s: str) -> str:
        _dict = defaultdict(int)

        for c in s:
            _dict[c] += 1

        _list = [item for item in _dict.items()]
        _list = sorted(_list, key=lambda item: item[1], reverse=True)

        return "".join([item[0] * item[1] for item in _list])

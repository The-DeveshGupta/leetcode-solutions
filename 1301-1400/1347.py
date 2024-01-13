class Solution:
    def minSteps(self, s: str, t: str) -> int:
        _dict = defaultdict(int)
        output = 0

        for char1, char2 in zip(s, t):
            _dict[char1] += 1
            _dict[char2] -= 1

        for num in _dict.values():
            output += num if num > 0 else 0

        return output

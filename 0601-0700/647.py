class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        output = 0

        for i in range(size):
            for j in range(i, size):
                if self.palindrone(s[i:j + 1]):
                    output += 1

        return output

    def palindrone(self, s):
        return s == s[::-1]

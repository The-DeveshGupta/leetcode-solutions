class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        hl = len(s) // 2
        alike = 0

        for i in range(hl):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                alike -= 1
            if s[i + hl] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                alike += 1

        return alike == 0

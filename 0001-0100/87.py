class Solution:
    dp = {}

    def isScramble(self, s1: str, s2: str) -> bool:

        key = s1 + '*' + s2
        if key in self.dp.keys():
            return self.dp[key]

        dictionarize = [0] * 26
        l = len(s1)
        output = False

        for i in range(l):
            dictionarize[ord(s1[i]) - 97] += 1
            dictionarize[ord(s2[i]) - 97] -= 1
        if max(dictionarize):
            return False
        if s1 == s2:
            return True

        for i in range(1, l):
            output = output or (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (
                        self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]))

        self.dp[key] = output
        return output

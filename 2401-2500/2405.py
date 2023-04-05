class Solution:
    def partitionString(self, s: str) -> int:

        unique_substring = 0
        dict = [0] * 26

        for char in s:
            if dict[ord(char) - 97]:
                dict = [0] * 26
                unique_substring += 1
            dict[ord(char) - 97] = 1
        else:
            if sum(dict):
                unique_substring += 1

        return unique_substring

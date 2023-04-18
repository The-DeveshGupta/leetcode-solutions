class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for a,b in zip(word1, word2):
            output += a + b
        return output + word1[len(output)//2:] + word2[len(output)//2:]

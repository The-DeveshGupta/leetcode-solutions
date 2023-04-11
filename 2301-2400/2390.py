class Solution:
    def removeStars(self, s: str) -> str:
        stack = ""
        for char in s:
            if char == '*':
                stack = stack[:-1]
            else:
                stack += char
        return stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        for char in s:
            if char in '({[':
                stack += char
            else:
                if len(stack) == 0:
                    return False
                if char == ')' and stack[-1] == '(' or char == '}' and stack[-1] == '{' or char == ']' and stack[-1] == '[':
                    stack = stack[:-1]
                else:
                    return False
        return len(stack) == 0

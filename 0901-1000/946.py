class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push_idx = 0
        pop_idx = 0
        while push_idx < len(pushed):
            stack.append(pushed[push_idx])
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
            push_idx += 1

        return len(stack) == 0

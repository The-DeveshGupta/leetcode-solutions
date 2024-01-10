# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            d1, a1 = dfs(node.left)
            d2, a2 = dfs(node.right)
            if node.val == start:
                return max(d1, d2), 1
            else:
                if a1:
                    return max(d1, d2 + a1), (a1 + a2) + 1
                elif a2:
                    return max(d1 + a2, d2), (a1 + a2) + 1
                else:
                    return max(d1, d2) + 1, 0

        d, a = dfs(root)
        return max(d, a - 1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        output = 0

        def bfs(node, c_sum):
            nonlocal output
            if not node:
                return
            c_sum = c_sum * 10 + node.val
            if node.left or node.right:
                bfs(node.left, c_sum)
                bfs(node.right, c_sum)
            else:
                output += c_sum

        bfs(root, 0)

        return output

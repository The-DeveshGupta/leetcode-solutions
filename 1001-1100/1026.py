# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_v = 0

    def parseTree(self, node):
        low, high = node.val, node.val

        if node.left:
            left_low, left_high = self.parseTree(node.left)
            low = min(low, left_low)
            high = max(high, left_high)
        if node.right:
            right_low, right_high = self.parseTree(node.right)
            low = min(low, right_low)
            high = max(high, right_high)

        self.max_v = max(self.max_v, abs(node.val - low), abs(high - node.val))
        return low, high

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.parseTree(root)
        return self.max_v

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror_node(left_node, right_node):
            if left_node and right_node:
                return (left_node.val == right_node.val) and is_mirror_node(left_node.left,
                                                                            right_node.right) and is_mirror_node(
                    left_node.right, right_node.left)
            else:
                return left_node == right_node

        return is_mirror_node(root.left, root.right)

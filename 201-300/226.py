# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def bfs(root, new_root):
            if root.left:
                new_root.right = TreeNode(root.left.val)
                bfs(root.left, new_root.right)
            if root.right:
                new_root.left = TreeNode(root.right.val)
                bfs(root.right, new_root.left)

        new_root = None

        if root:
            new_root = TreeNode(val=root.val)
            bfs(root, new_root)

        return new_root
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        total = 0
        if low <= root.val <= high:
            total += root.val
        total += self.rangeSumBST(root.left, low, high)
        total += self.rangeSumBST(root.right, low, high)
        return total

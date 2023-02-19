# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        level = defaultdict(list)

        def bfs(root, loop):
            level[loop].append(root.val)
            if root.left:
                bfs(root.left, loop+1)
            if root.right:
                bfs(root.right, loop+1)

        if root:
            bfs(root, 1)

        output = []

        if len(level.keys()) == 0:
            return output

        for i in range(max(level.keys())):
            if i % 2:
                output.append(level[i+1][::-1])
            else:
                output.append(level[i+1])

        return output

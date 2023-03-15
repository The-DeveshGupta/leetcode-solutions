# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        flag = True
        queue = [root]

        while queue:
            if not flag and queue[0]:
                break
            if not queue[0]:
                flag = False
            else:
                queue.append(queue[0].left)
                queue.append(queue[0].right)
            queue.pop(0)
        else:
            return True
        return False

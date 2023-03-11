# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None
        if not head.next:
            return TreeNode(val=head.val)

        slow_pointer = head
        fast_pointer = head.next.next

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        root = TreeNode(val=slow_pointer.next.val)

        right_side = slow_pointer.next.next
        slow_pointer.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right_side)

        return root

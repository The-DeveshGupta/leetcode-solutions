# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.len = 0
        temp = head
        while temp:
            self.len += 1
            temp = temp.next

    def getRandom(self) -> int:
        idx = random.randint(1, self.len)
        temp = self.head
        for _ in range(1, idx):
            temp = temp.next
        return temp.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

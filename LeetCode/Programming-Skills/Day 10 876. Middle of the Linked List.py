# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        count = 0
        while x:
            count += 1
            x = x.next
        count = count//2

        for i in range(count):
            head = head.next
        return head

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast: ListNode = head
        slow: ListNode = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next


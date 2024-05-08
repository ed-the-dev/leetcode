from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow: ListNode = head
        fast: ListNode = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        
        return False
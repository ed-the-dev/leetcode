from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow: ListNode = head
        fast: ListNode = head

        meeting_node: ListNode = None

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                meeting_node = slow
                break

        if meeting_node:

            slow_2: ListNode = head

            while True:

                if slow_2 is meeting_node:
                    return slow_2
                
                slow_2 = slow_2.next
                meeting_node = meeting_node.next
        
        return 
            

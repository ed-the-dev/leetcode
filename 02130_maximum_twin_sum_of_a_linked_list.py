from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # Should instead iterate through reversing the first half and using slow and fast to find the midpoint,
        # then I can continue going on incrementing one in each direction and check the sum.
        
        slow: ListNode = head
        fast: ListNode = head

        prev: ListNode = None

        max_twin_sum: int = 0

        right_pntr: ListNode = fast

        while fast is not None and fast.next is not None:

            fast = fast.next.next

            right_pntr = slow.next
            
            next = slow.next

            slow.next = prev

            prev = slow

            slow = next

        left_pntr: ListNode = prev

        while left_pntr is not None:

            current_twin_sum: int = left_pntr.val + right_pntr.val

            max_twin_sum = max(max_twin_sum, current_twin_sum)

            left_pntr = left_pntr.next
            right_pntr = right_pntr.next

        return max_twin_sum


solution: Solution = Solution()

ln: ListNode = ListNode(100000)

head: ListNode = ListNode(1, ln)

print(solution.pairSum(head))

    

# [47,22,81,
 
#  46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,

#  81,5,9]
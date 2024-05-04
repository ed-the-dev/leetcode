from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result: ListNode = ListNode()

        current: ListNode = result

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next
            
        while list1:
            current.next = ListNode(list1.val)
            current = current.next
            list1 = list1.next


        while list2:
            current.next = ListNode(list2.val)
            current = current.next
            list2 = list2.next

        return result.next
    

solution: Solution = Solution()


l14: ListNode = ListNode(4)
l12: ListNode = ListNode(2, l14)
l11: ListNode = ListNode(1, l12)

l24: ListNode = ListNode(4)
l23: ListNode = ListNode(3, l24)
l21: ListNode = ListNode(1, l23)

print(solution.mergeTwoLists(l11, l21))
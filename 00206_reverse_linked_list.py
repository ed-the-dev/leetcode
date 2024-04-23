from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    def __str__(self):
        return "Value: %s\n Next's Value: %s" % (self.val, self.next.val)
    
    def __repr__(self):
        # Build a concise string representation (similar to default behavior)
        return "Value: %s\n Next's Value: %s" % (self.val, self.next.val)

def reverseListIterative(head: Optional[ListNode]) -> Optional[ListNode]:

    prev: ListNode = None
    current_node: ListNode = head

    while current_node:

        next_node = current_node.next

        # Point to the previous node
        current_node.next = prev

        prev = current_node
        
        # move onto the next node.
        current_node = next_node

    return prev


def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:

    def reverse(cur: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:

        # Base case
        if cur is None:
            return prev
        
        else:
            next = cur.next
            cur.next = prev
            return reverse(next, cur)

    return reverse(head, None)



node_5: ListNode = ListNode(val=5)
node_4: ListNode = ListNode(val=4, next=node_5)
node_3: ListNode = ListNode(val=3, next=node_4)
node_2: ListNode = ListNode(val=2, next=node_3)
node_1: ListNode = ListNode(val=1, next=node_2)

result: ListNode = reverseListRecursive(node_1)
result2 = reverseListRecursive(None)

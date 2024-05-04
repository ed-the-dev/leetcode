class ListNode:

    def __init__(self, value: int = 0, next = None, prev = None) -> None:
        self.value = value
        self.next: ListNode = next
        self.prev: ListNode = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail  = ListNode(0)

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:

        count = -1
        current: ListNode = self.head 
        while count < index and current != None:
            current = current.next
            count += 1

        if current and current is not self.tail:
            return current.value

        return -1
        

    def addAtHead(self, val: int) -> None:

        new_node: ListNode = ListNode(val, self.head.next, self.head)
        
        self.head.next.prev = new_node
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:

        new_node: ListNode = ListNode(val, self.tail, self.tail.prev)

        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:

        new_node: ListNode = ListNode(val)

        current: ListNode = self.head
        count: int = -1
        while count < index and current != None:
            current = current.next
            count += 1

        if count == index and current != None:

            prev: ListNode = current.prev

            new_node.next = current
            new_node.prev = prev

            prev.next = new_node
            current.prev = new_node

        

    def deleteAtIndex(self, index: int) -> None:

        count: int = -1
        current: ListNode = self.head

        while count < index and current != None:
            current = current.next
            count += 1

        
        if current and current is not self.tail:
            next: ListNode = current.next
            prev: ListNode = current.prev

            next.prev = prev
            prev.next = next


linked_list: MyLinkedList = MyLinkedList()

linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.addAtIndex(3,2)
print(linked_list.get(1))
linked_list.deleteAtIndex(1)

print(linked_list.get(1))

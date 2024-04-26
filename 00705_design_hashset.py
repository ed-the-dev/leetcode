from typing import Optional

# Nice trick here and probably with all lists of linked lists is to have a dummy starter node,
# then you can loop through with 
# while node.next:

# Separate Chaining Solution:

class ListNode:

    def __init__(self, value):
        self.value: int = value
        self.next: Optional[ListNode] = None

class MyHashSet:

    def __init__(self):

        self.size: int = 0
        self.capacity: int = 2

        self.hashset: list[ListNode] = [ListNode(0), ListNode(0)]

    def hash(self, key: int) -> int:

        index:int = key % self.capacity
        return index

    def rehash(self):
        
        # Double the capacity.
        self.capacity = self.capacity * 2

        copy: list[ListNode] = self.hashset

        # Re-initialise hashset variables
        self.hashset = [ListNode(0) for _ in range(0, self.capacity)]
        self.size = 0

        for node in copy:
            while node.next:
                self.add(node.next.value)
                node = node.next
        

    def add(self, key: int) -> None:

        index = self.hash(key)

        current_node: ListNode = self.hashset[index]
        
        # Get to the tail of the linked list 
        while current_node.next:

            # If the key already exists then stop
            if current_node.next.value == key:
                return
            
            current_node = current_node.next
        
        new_node: ListNode = ListNode(key)
        current_node.next = new_node

        self.size += 1
        if self.capacity // 2 < self.size:
            self.rehash()
        

    def remove(self, key: int) -> None:

        index = self.hash(key)

        current_node: ListNode = self.hashset[index]

        while current_node.next:
            if current_node.next.value == key:
                # Update pointers to remove Node from linked list. Garbage collection assumed to clean up.
                current_node.next = current_node.next.next
                self.size -= 1
                return
            current_node = current_node.next

        

    def contains(self, key: int) -> bool:

        index = self.hash(key)

        current_node: ListNode = self.hashset[index]

        while current_node.next:
            if current_node.next.value == key:
                return True
            current_node = current_node.next

        return False
    
hash_set: MyHashSet = MyHashSet()

print("Add 1")
hash_set.add(1)

print("Add 2")
hash_set.add(2)

print("Contains 1: %s " % hash_set.contains(1))
print("Contains 3: %s " % hash_set.contains(3))

print("Add 2 Again")
hash_set.add(2)
print("Contains 2: %s " % hash_set.contains(2))

hash_set.remove(2)
print("Contains 2: %s " % hash_set.contains(2))

print(hash_set.hashset)


# Open Addressing Solution:
# The remove function has a bug where if you remove an element, you would then need to shift elements
# back up otherwise they would return null.

# This is basically a pain in the bum to implement so better to go with the Separate Chaining solution.

class MyHashSetOpenAddressing:

    def __init__(self):

        self.size: int = 0
        self.capacity: int = 2

        self.hashset: list[Optional[int]] = [None, None]

    def hash(self, key: int) -> int:

        index:int = key % self.capacity
        return index

    def rehash(self):
        
        self.capacity = self.capacity * 2

        copy = self.hashset

        self.hashset = [None for _ in range(0, self.capacity)]

        for num in copy:
            if num is not None:
                self.add(num)

        return 
        

    def add(self, key: int) -> None:

        index = self.hash(key)

        while True:

            if self.hashset[index] == None:

                self.hashset[index] = key
                self.size += 1
                if self.capacity // 2 < self.size:
                    self.rehash()
                return
            
            else:
                if self.hashset[index] == key:
                    return
                else:
                    index += 1
                    index = index % self.capacity

        

    def remove(self, key: int) -> None:

        if self.contains(key):

            index = self.hash(key)

            # 'is not None' for the case where the key is 0
            while self.hashset[index] is not None:
                if self.hashset[index] == key:
                    self.hashset[index] = None
                    self.size -= 1
                else:
                    index += 1
                    index = index % self.capacity


        

    def contains(self, key: int) -> bool:

        index = self.hash(key)
        
        # 'is not None' for the case where the key is 0
        while self.hashset[index] is not None:
            if self.hashset[index] == key:
                return True
            else:
                index += 1
                index = index % self.capacity
            
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



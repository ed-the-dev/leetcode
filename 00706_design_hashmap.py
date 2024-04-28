class ListNode:

    def __init__(self, key: int, value: int):

        self.key: int = key
        self.value: int = value
        self.next: ListNode = None

class MyHashMap:

    def __init__(self):
        self.size: int = 0
        self.capacity: int = 2
        self.hashmap: list[ListNode] = [ListNode(0,0) for _ in range(0,self.capacity)]

    def hash(self, key: int):
        index = key % self.capacity
        return index
    
    def rehash(self):

        copy: list[ListNode] = self.hashmap

        self.capacity = self.capacity * 2
        self.size = 0

        self.hashmap = [ListNode(0,0) for _ in range(0,self.capacity)]

        for list_node in copy:
            while list_node.next:
                self.put(list_node.next.key, list_node.next.value)
                list_node = list_node.next

    def put(self, key: int, value: int) -> None:

        index = self.hash(key)

        current_node: ListNode = self.hashmap[index]

        while current_node.next:
            if current_node.next.key == key:
                current_node.next.value = value
                return
            current_node = current_node.next
        
        new_node: ListNode = ListNode(key, value)

        current_node.next = new_node

        self.size += 1
        if self.capacity // 2 < self.size:
            self.rehash()
        

    def get(self, key: int) -> int:

        index = self.hash(key)

        current_node: ListNode = self.hashmap[index]
        while current_node.next:
            if current_node.next.key == key:
                return current_node.next.value
            current_node = current_node.next

        return -1
        

    def remove(self, key: int) -> None:

        index = self.hash(key)

        current_node: ListNode = self.hashmap[index]

        while current_node.next:
            if current_node.next.key == key:

                current_node.next = current_node.next.next
                self.size -=1

                return
            current_node = current_node.next

        return



hash_map: MyHashMap = MyHashMap()

hash_map.put(1,1) 
hash_map.put(2,2)
print(hash_map.get(1))
print(hash_map.get(2))
print(hash_map.get(3))
hash_map.put(2,1)
print(hash_map.get(2))

hash_map.remove(2)
print(hash_map.get(2))




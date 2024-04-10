class Node:

    def __init__(self, key, value):
        self.key, self.value = key, value

        self.prev: Node
        self.next: Node

        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}

        # Left represents LRU, Right represents MRU.
        self.left = self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node):

        next: Node = node.next
        prev: Node = node.prev

        next.prev = prev
        prev.next = next

    def insert(self, node: Node) -> Node:

        node.prev = self.right.prev
        node.next = self.right

        self.right.prev.next = node
        self.right.prev = node

        return node
        

    def get(self, key: int) -> int:
        if key in self.cache:

            import pdb
            pdb.set_trace()

            result_node: Node = self.cache[key]

            self.remove(result_node)
            result_node = self.insert(result_node)
            self.cache[key] = result_node

            return result_node.value
        
        else: 
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:

            target_node: Node = self.cache[key]

            self.remove(target_node)
            target_node.value = value
            self.insert(target_node)
            self.cache[key] = target_node
        else:
            if len(self.cache) >= self.capacity:

                # Get LRU
                lru: Node = self.left.next
                self.remove(lru)
                self.cache.pop(lru.key)
            
            new_node: Node = Node(key, value)
            new_node = self.insert(new_node)
            self.cache[key] = new_node


                


lru_cache: LRUCache = LRUCache(2)
lru_cache.put(1,1)
lru_cache.put(2,2)
print(lru_cache.get(1))
lru_cache.put(3,3)
print(lru_cache.get(2))
lru_cache.put(4,4)
print(lru_cache.get(1))
print(lru_cache.get(3))
print(lru_cache.get(4))


print(lru_cache)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
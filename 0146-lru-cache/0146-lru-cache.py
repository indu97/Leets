class LRUCache:
    class DLLNode:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.head = None    #LRU
        self.tail = None    #MRU
        self.capacity = capacity
        self.occupance = 0
        self.pos = {}       # key -> DLLNode

    def appendAtTail(self, node):
        node.next = None
        node.prev = None
        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def deleteNode(self, node):
        if node is self.head and node is self.tail:     # Only node in the list
            self.head = self.tail = None
        elif node.prev and node.next:                   
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.prev:
            node.prev.next = None
            self.tail = node.prev
        elif node.next:
            node.next.prev = None
            self.head = node.next

    def get(self, key: int) -> int:
        if key in self.pos:
            node = self.pos[key]
            # Remove the node from the current position
            self.deleteNode(node)

            # Append at the end
            self.appendAtTail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        # If key exists - udpate, delete from current pos and append at the end
        if key in self.pos:
            node = self.pos[key]
            node.value = value
            self.deleteNode(node)
            self.appendAtTail(node)

        # else - create and append at the end 
        else:
            # If out of capacity - remove LRU
            if self.occupance >= self.capacity:
                # Remove the LRU at head
                lru = self.head
                self.deleteNode(lru)
                del self.pos[lru.key]

                # Reduce occupance by 1
                self.occupance -= 1

            # Create new node
            newNode = self.DLLNode(key, value)

            # Append at tail
            self.appendAtTail(newNode)

            # Add it to the hashmap
            self.pos[key] = newNode

            # Increase occupance by 1
            self.occupance += 1
        




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
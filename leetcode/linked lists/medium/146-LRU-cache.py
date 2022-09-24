class Node:
    
    def __init__(self, data, key):
        self.val = data
        self.key = key
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.lru, self.mru = Node(0, 0), Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru
        

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insert(self, node):
        prev = self.mru.prev
        nxt = self.mru
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(value, key)
        self.insert(self.cache[key])
            
        if len(self.cache) > self.cap:
            leastRecentlyUsed = self.lru.next
            self.remove(leastRecentlyUsed)
            del self.cache[leastRecentlyUsed.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
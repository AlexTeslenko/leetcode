class DoubltLinkedNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DoubltLinkedNode(), DoubltLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node
        
    def _remove_node(self, node):
        prev = node.prev
        nxt = node.next
        
        prev.next = nxt
        nxt.prev = prev
        
    def _move_node_to_start(self, node):
        self._remove_node(node)
        self._add_node(node)
        
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        
        return res

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            self._move_node_to_start(node)
            return node.value
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node =  self.cache[key]
            node.value = value
            self._move_node_to_start(node)
        
        else:
            new_node = DoubltLinkedNode()
            new_node.key = key
            new_node.value = value
            self.cache[key] = new_node
            
            self._add_node(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
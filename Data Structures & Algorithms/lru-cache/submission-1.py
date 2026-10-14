class Node:
    def __init__(self,key,value,next=None,prev=None):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,curr):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    
    def insert(self,node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

        
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        curr = self.cache[key]
        self.remove(curr)
        self.insert(curr)
        return curr.value

        

    def put(self, key: int, value: int) -> None:
        if not key in self.cache:
            new_node = Node(key,value)
            self.insert(new_node)
            self.cache[key] = new_node

            if len(self.cache)>self.capacity:
                lru = self.tail.prev
                self.remove(self.tail.prev)
                del self.cache[lru.key]
        else:
            curr = self.cache[key]
            curr.value = value
            self.remove(curr)
            self.insert(curr)

        

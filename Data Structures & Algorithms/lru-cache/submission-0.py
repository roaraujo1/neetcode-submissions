class Node:
    def __init__(self,key,val,next=None,prev=None):
        self.key = key
        self.val = val
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity 
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self,node):
        nxt = self.head.next
        node.next = nxt
        node.prev = self.head
        self.head.next = node
        nxt.prev = node

        
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        curr = self.cache[key]
        self.remove(curr)
        self.insert(curr)
        return curr.val
        
    def put(self, key: int, value: int) -> None:
        if not key in self.cache:
            new_node = Node(key,value)
            self.insert(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.remove(self.tail.prev)
                del self.cache[lru.key]
        else:
            curr = self.cache[key]
            curr.val = value
            self.remove(curr)
            self.insert(curr)



        

class Node:
    def __init__(self, key,value,next=None,prev=None):
        self.key = key
        self.value =value
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self,node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.insert(new_node)
            if len(self.cache) > self.capacity:
                node_remove = self.tail.prev
                self.remove(self.tail.prev)
                del self.cache[node_remove.key]
        else:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)

            

        

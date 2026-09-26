"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cache = {}

        def dfs(node):
            if not node:
                return 
            
            if node in cache:
                return cache[node]
            
            temp = Node(node.val)
            cache[node] = temp
            

            for i in node.neighbors:
                temp.neighbors.append(dfs(i))
            return temp
        
        dfs(node)
        return cache[node]
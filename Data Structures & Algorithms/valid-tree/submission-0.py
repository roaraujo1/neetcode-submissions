class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        visited=set()

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node,prevNode):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj[node]:
                if nei == prevNode:
                    continue
                
                if not dfs(nei,node):
                    return False
            return True
        
        return  dfs(0,None) and len(visited)==n


        


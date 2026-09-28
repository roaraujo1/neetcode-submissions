class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = collections.defaultdict(list)
        res = 0

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res+=1
        
        return res 

        
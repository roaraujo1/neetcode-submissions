from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
        def bfs(r,c):
            if r == len(grid) or r<0 or c < 0 or c == len(grid[0]) or (r,c) in visited or grid[r][c]==0:
                return 
            if grid[r][c] == 1:
                grid[r][c] = 2
            
           
            visited.add((r,c))
            queue.append((r,c))
        
        while queue:
            ln = len(queue)
    
            for _ in range(ln):
                row,col = queue.popleft()

                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in directions:
                    newR,newC = row+dr,col+dc
                    bfs(newR,newC)
            if queue:
                time+=1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return time
            


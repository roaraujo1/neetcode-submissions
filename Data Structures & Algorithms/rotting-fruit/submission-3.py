from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        queue = deque()
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append([r,c])
                if grid[r][c] == 1:
                    count+=1
                
        while queue:
            qlen = len(queue)
            rotted = False
            for _ in range(qlen):
                fruit = queue.popleft()
                row,col = fruit[0],fruit[1]
                
                directions=[(0,1),(1, 0),(-1,0),(0, -1)]
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if new_row < len(grid) and new_row>=0 and new_col < len(grid[0]) and new_col>= 0:
                        if grid[new_row][new_col] == 1:
                            count-=1
                            rotted =True
                            queue.append([new_row,new_col])
                            grid[new_row][new_col] = 2
            if rotted:
                time+=1
            
        if count>0:
            return -1
        return time





    

    
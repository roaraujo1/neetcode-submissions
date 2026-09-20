class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == "1":
                    islands+=1
                    self.dfs(grid,r,c)
        
        return islands

    
    def dfs(self,grid,row,col):
        if not(row < len(grid) and col < len(grid[0]) and row >= 0 and col >= 0):
            return

        if grid[row][col] =="0":
            return 

        grid[row][col] = "0"
        self.dfs(grid,row+1,col)
        self.dfs(grid,row-1,col)
        self.dfs(grid,row,col-1)
        self.dfs(grid,row,col+1)


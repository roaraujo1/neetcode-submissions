class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def helper(grid,r,c,memo):
            if (r,c) in memo:
                return memo[(r,c)]
            if r == len(grid) or c == len(grid[0]):
                return float("inf")
            if r == len(grid)-1 and c == len(grid[0])-1:
                return grid[r][c]
            

            down = helper(grid,r+1,c,memo)
            right = helper(grid,r,c+1,memo)

            memo[(r,c)]= grid[r][c] + min(down,right)
            return memo[r,c]
        return helper(grid,0,0,{})

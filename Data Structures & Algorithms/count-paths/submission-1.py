class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def helper(r,c,memo):
            if (r,c) in memo:
                return memo[(r,c)]
            if r == m or c == n:
                return 0
            
            if r == m-1 and c == n-1:
                return 1
            
            down = helper(r+1,c,memo)
            right = helper(r,c+1,memo)
            memo[(r,c)] = down+right
            return memo[(r,c)]
        return helper(0,0,{})

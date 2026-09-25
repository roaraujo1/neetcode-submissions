class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res,sol = [], []

        def backtracking(i,curr):
            if curr == target:
                res.append(sol[:])
                return
            if i == n or curr>target:
                return 
            
            
            sol.append(nums[i])
            backtracking(i,curr+nums[i])
            sol.pop()
           
            
            backtracking(i+1,curr)
            
        backtracking(0,0)
        
        return res




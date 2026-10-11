class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def helper(i,memo):
            if i in memo:
                return memo[i]
            if i +1 >= len(nums):
                return True
            
            
            for j in range(1,nums[i]+1):
                if helper(j+i,memo):
                    return True
            

            memo[i] = False
            return memo[i]
        

      
        return helper(0,{})

        

        
       
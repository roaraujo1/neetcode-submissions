class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def helper(i,j,memo):
            key = (i,j)
            if key in memo:
                return memo[key]

            if i == j:
                return 0
            if j == len(nums) or i ==len(nums):
                return 0
            if nums[i] < nums[j]:
                memo[key] =  max(1+helper(j,j+1,memo),helper(i,j+1,memo))
            if nums[i] >= nums[j]:
                memo[key] = helper(i,j+1,memo)
            return memo[key]
        memo = {}
        maxRes = float("-inf")
        for i in range(len(nums)):
            maxRes = max(maxRes,1+helper(i,i+1,memo))
        
        return maxRes
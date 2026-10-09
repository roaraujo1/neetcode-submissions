class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robber(arr):
            memo = {}
            def dfs(i):
                if i < 0:
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(arr[i]+dfs(i-2),dfs(i-1))
                return memo[i]
        
            return dfs(len(arr)-1)
        return max(robber(nums[1::]),robber(nums[:len(nums)-1]))
    
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(i,target,arr):
           
            if target < 0:
                return 
            if target == 0:
                res.append(arr.copy())
                return 
            
            for j in range(i,len(nums)):
                arr.append(nums[j])
                helper(j,target-nums[j],arr)
                arr.pop()
           
        helper(0,target,[])
        return res
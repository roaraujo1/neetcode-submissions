class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
       
        big = small =nums[0]
        maxRes = nums[0]

        for i in nums[1::]:

            temp = max(i*small,i*big,i)
            small = min(i*small,i*big,i)
            big = temp
            maxRes = max(big,maxRes)
        return maxRes
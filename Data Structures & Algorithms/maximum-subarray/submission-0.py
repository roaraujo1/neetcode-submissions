class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        curSum = 0

        for i in nums:
            curSum+=i
            if curSum < i:
                curSum = i
            maxSum = max(maxSum,curSum)
        return maxSum
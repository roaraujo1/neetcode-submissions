class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0

        left = 0
        right = 1

        while right<len(prices):
            if prices[left]>prices[right]:
                left = right
            else:
                prof = max(prof,prices[right]-prices[left])
            right+=1
        return prof
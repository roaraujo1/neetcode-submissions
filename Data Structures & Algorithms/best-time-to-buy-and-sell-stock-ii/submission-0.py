class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1
        res = 0

        while right <=len(prices)-1:
            if prices[left] < prices[right]:
                res+= prices[right] - prices[left]

            left=right
            right+=1
        return res
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        maxProf = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                maxProf = max(maxProf,prices[sell]-prices[buy])
            sell+=1
            print(sell)
        return maxProf

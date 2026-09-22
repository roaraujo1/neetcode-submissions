class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo ={}

        def dp(amount):
            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            curMin = float("inf")
            for i in coins:
               curMin = min(curMin,1+dp(amount-i))
            
            memo[amount] = curMin
            return curMin
        
        res=dp(amount)
        if res == float("inf"):
            return -1
        return res
        

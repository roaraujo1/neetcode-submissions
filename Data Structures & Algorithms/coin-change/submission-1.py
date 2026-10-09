class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def helper(coins,amount,memo):
            
            if amount in memo:
                return memo[amount]
            if amount ==0:
                return 0
            if amount < 0:
                return float("inf")
            
            min_ = float("inf")
            for i in coins:
                
                min_ = min(min_,1+ helper(coins,amount-i,memo))
            
            memo[amount] = min_
            return memo[amount]
        
        res =helper(coins,amount,{})
        if res == float("inf"):
            return -1
        return res


            






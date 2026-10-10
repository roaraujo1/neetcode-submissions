class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def helper(coins,amount,i,memo):
            key = (amount,i)
            if key in memo:
                return memo[key]
            if amount == 0:
                return 0 
            if amount < 0 or i == len(coins):
                return float("inf")
            
            coin = coins[i]
            minRes = float("inf")
            for j in range(0,(amount//coin)+1):
                rem = amount - (j*coin)
                num_res = helper(coins,rem,i+1,memo)
                minRes = min(minRes,num_res+j)
            memo[key] = minRes
            return minRes
        res = helper(coins,amount,0,{})
        if res == float("inf"):
            return -1
        return res 


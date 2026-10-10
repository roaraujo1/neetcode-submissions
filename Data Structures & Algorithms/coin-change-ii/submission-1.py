class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def helper(amount,coins,i,memo):
            key = (amount,i)
            if key in memo:
                return memo[key]
            if amount == 0:
                return 1
            if amount < 0 or i == len(coins):
                return 0
            
            coin = coins[i]
            total = 0
            for j in range(0,(amount//coin)+1):
                rem = amount - (j*coin)
                total += helper(rem,coins,i+1,memo)
            memo[key] = total
            return total
        return helper(amount,coins,0,{})
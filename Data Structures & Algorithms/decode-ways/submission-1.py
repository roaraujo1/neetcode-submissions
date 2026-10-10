class Solution:
    def numDecodings(self, s: str) -> int:
        
        def helper(i,memo):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == "0":
                return 0 
            temp = helper(i+1,memo)
            temp2 = helper(i+2,memo)
            if s[i:i+2] <= "26":
                memo[i] = temp + temp2
            else:
                memo[i] = temp
            return memo[i]

        return helper(0,{})
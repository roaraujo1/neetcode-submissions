class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def helper(i,j,memo):
            key = (i,j)
            if key in memo:
                return memo[key]
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                memo[key] = 1 + helper(i+1,j+1,memo)
            
            if text1[i]!=text2[j]:
                memo[key] = max(helper(i,j+1,memo),helper(i+1,j,memo))
            return memo[key]
        return helper(0,0,{})
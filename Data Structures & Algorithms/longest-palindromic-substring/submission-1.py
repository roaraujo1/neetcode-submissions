class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] *len(s) for _ in range(len(s))]
        res = ""
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if len(res) < len(s[i:j+1]):
                        res = s[i:j+1]
        return res

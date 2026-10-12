class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dups = set()
        left = 0
        res = 0

        for right in range(len(s)):

            while s[right] in dups:
                dups.remove(s[left])
                left+=1

            dups.add(s[right])
            res = max(res,len(dups))
        return res








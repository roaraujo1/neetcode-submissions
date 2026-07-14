class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        longest = 0

        left =  0

        for right in range(len(s)):
            
            
           
            
            while s[right] in myset and myset:
                myset.remove(s[left])
                left+=1
            myset.add(s[right])
            longest = max(longest,len(myset))
        
        return longest
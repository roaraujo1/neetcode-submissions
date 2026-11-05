class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        maxLength = 0

        for i in range(len(s)):
            window[s[i]] = 1+window.get(s[i],0)
            maxVal = max(window.values())
            
            while (i-left+1)-maxVal > k:
                window[s[left]]-=1
                left+=1
            
            
            maxLength = max(maxLength,(i-left+1))
        return maxLength
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxFreq = 0
        res = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
            maxFreq = max(maxFreq,count[s[i]])
            
            if (i-left+1) - maxFreq  > k:
                count[s[left]]-=1
                left+=1
            res = max(res,i-left+1)
        
        return res

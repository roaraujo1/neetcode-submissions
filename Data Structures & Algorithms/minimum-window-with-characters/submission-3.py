class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        count_t = Counter(t)
        count = {}
        left =0
        min_index = -1
        min_len =float("inf")
        have = 0
        need = len(count_t)

        for r in range(len(s)):
            if s[r] in t:
                count[s[r]] = 1+count.get(s[r],0)
                if count[s[r]] == count_t[s[r]]:
                    have+=1
            while have == need:
                w = r-left+1
                if w < min_len:
                    min_len = w
                    min_index = left
                
                if s[left] in t:
                    count[s[left]]-=1
                    if count[s[left]]<count_t[s[left]]:
                        have-=1
                left+=1
        if min_len == float('inf'): return ""
        return s[min_index:min_index+min_len]

            

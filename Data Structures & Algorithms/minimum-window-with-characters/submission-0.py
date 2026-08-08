class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        length_window = float('inf')
        count = collections.defaultdict(int)

        need = set(t)
        have = 0

        left = 0
        res = ""

        for i in range(len(s)):
            count[s[i]]+=1

            if s[i] in t_count and count[s[i]] == t_count[s[i]]:
                have+=1
            
            while len(need) == have:
                if i-left+1 < length_window:
                    length_window = i-left+1
                    res= s[left:i+1]


               
                count[s[left]]-=1
                if s[left] in t_count and count[s[left]] < t_count[s[left]]:
                    have-=1
                left+=1
        return res



            
        
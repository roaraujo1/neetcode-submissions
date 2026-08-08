class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_count = Counter(s1)
        count = collections.defaultdict(int)

        for right in range(len(s2)):
            count[s2[right]]+=1
            print(count)
            if right - left +1 == len(s1):
                if count == s1_count:
                    return True
                if count[s2[left]] <=1:
                    del count[s2[left]]
                else:
                    count[s2[left]]-=1
                left+=1
                
              
        
        return False
            
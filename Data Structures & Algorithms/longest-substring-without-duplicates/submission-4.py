class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
         1. intialize set, left pointer,res
         2. for loop
            - it has the right pointer
            - adding to the set
            - checking to see if the window is not valid
                - if the char is already in set then invalid
         3. return res

         zxyzxyz

         set = (y,z)
         left = 2
         res = 3

         for right in range(len(s)):

            while s[right] in set:
                
                set.remove[s[left]]
                left+=1
            
            set.add(s[right])
            res = max(res,len(set))


        '''


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








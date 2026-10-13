import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minH = float("inf")
        maxNum = max(piles)


        left,right = 1,maxNum

        while left<=right:
            mid = (left+right)//2
            cur = 0

            for i in piles:
                
                cur += math.ceil(i/mid)
            
        
            if cur <= h:
                right = mid -1
                minH = min(minH,mid)
                
            else:
                left = mid +1
            

            
        return minH




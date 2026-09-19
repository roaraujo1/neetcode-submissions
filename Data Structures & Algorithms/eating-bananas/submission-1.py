import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_num = max(piles)+1
        left = 1
        right = max_num
        smallest = max_num 

        while left<=right:
            mid = (right+left)//2
            curr_value = 0

            for i in piles:
                curr_value+= math.ceil(i/mid)
                if curr_value>h:
                    break 
            
            if curr_value > h:
                left = mid+1
            else:
                right = mid -1
                #smallest = min(smallest,mid)
        return left

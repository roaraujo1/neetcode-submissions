class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {}

        for i,v in enumerate(nums):
            if v in count:
                if abs(count[v]-i)<=k:
                    return True
                else:
                    False
            count[v] = i
        return False

        
        
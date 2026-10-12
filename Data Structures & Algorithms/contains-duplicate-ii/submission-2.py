class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dups = {}

        for i,v in enumerate(nums):
            if v in dups and abs(dups[v]-i)<=k:
                return True
            dups[v] = i
        return False
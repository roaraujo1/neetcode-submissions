class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i,v in enumerate(nums):
            rem = target - v

            if rem in cache:
                
                return [cache[rem],i]
            cache[v] = i
           
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cach = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in cach:
                return sorted([i,cach[rem]])
            cach[nums[i]]=i
        
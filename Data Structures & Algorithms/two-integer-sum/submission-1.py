class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i,v in enumerate(nums):
            diff = target - v
            if diff in store:
                return [store[diff],i]
            store[v] = i
        
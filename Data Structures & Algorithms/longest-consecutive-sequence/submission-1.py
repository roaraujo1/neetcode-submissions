class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res,temp = 0,0

        nums_set = set(nums)

        for i in nums_set:
            
            if i-1 not in nums_set:
                temp = 1
                while i +1 in nums_set:
                    i+=1
                    temp+=1
            
            res = max(res,temp)
        return res

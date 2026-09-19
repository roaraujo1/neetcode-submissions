class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (right+left)//2
            if nums[left]<nums[mid]:
                if nums[left]<nums[right]:
                    right = mid -1
                else:
                    left = mid +1

            else:
                if nums[mid]<=nums[right]:
                    right = mid
                else:
                    left = mid+1
        return nums[left]

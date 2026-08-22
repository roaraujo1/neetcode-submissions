class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1

        while left<=right:
            mid = (left+right)//2

            if target>= matrix[mid][0] and target<=matrix[mid][-1]:
                return self.binarySearch(matrix[mid],target)
            elif target < matrix[mid][0]:
                right = mid -1
            else:
                left = mid +1
        return False

    def binarySearch(self,curr,target):
        left = 0
        right = len(curr)-1

        while left <= right:
            mid = (left+right)//2

            if curr[mid] == target:
                return True
            elif curr[mid] < target:
                left = mid+1
            else:
                right = mid -1
        return False

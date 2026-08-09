class Solution:
    def binarySearch(self, curr_list: List, val: int) -> bool:
        left = 0
        right = len(curr_list)-1

        while left <=right:
            mid = (left+right)//2

            if curr_list[mid] == val:
                return True
            
            if curr_list[mid] < val:
                left = mid+1
            else:
                right = mid -1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1

        while left<=right:
            mid = (left+right)//2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
               return self.binarySearch(matrix[mid],target)
            
            elif target > matrix[mid][0]:
                left = mid +1
            else:
                right = mid -1
        return False

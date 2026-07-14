class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, arr, left, right):
        if left >= right:
            return
        pivot_index = self.partition(arr, left, right)
        self.quicksort(arr, left, pivot_index - 1)
        self.quicksort(arr, pivot_index + 1, right)

    def partition(self, arr, left, right):
        mid = (left + right) // 2
        arr[mid], arr[right] = arr[right], arr[mid]

        pivot = arr[right]
        i = left - 1

        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
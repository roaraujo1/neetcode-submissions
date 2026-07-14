class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #call quicksort 
        self.quicksort(nums,0,len(nums)-1)
        #return final result of nums 
        return nums

    def quicksort(self,nums,left,right):
        #base case
        if left >=right:
            return 
        #assign pivot
        pivot = self.partition(nums,left,right)
        #call quicksort on both left and right of pivot
        self.quicksort(nums,left,pivot-1)
        self.quicksort(nums,pivot+1,right)
        
    def partition(self,arr,left,right):
        #find the middle(pivot)
        mid = (left+right)//2
        #swap pivot with rightmost number
        arr[mid],arr[right] = arr[right],arr[mid]
        i = left-1
       
        #do a loop to interate through the array 
        for j in range(left,right):
            if arr[j]<arr[right]:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1], arr[right] = arr[right],arr[i+1]
        return i+1

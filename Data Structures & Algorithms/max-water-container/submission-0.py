class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left,right = 0,len(heights)-1
        while left<right:
            temp = min(heights[left],heights[right]) * (right-left)
            area = max(area,temp)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return area


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        left = 0
        right = len(height)-1

        leftMax= height[0]
        rightMax = height[right]

        while left<=right:
            leftMax = max(height[left],leftMax)
            rightMax = max(height[right],rightMax)

            if leftMax<=rightMax:
                res += abs(leftMax - min(height[left],height[right]))
                left+=1
            else:
                res += abs(rightMax - min(height[left],height[right]))
                right-=1
        return res
        


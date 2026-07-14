class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        

        temp = ""
        for i in s:
            if i.isalnum():
                temp+=i
        left = 0
        right = len(temp)-1
        
        while left<=right:
            if temp[left]!=temp[right]:
                return False
            left+=1
            right-=1
        return True
        


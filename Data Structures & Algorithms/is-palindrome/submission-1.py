class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        temp = ""
        
        for i in s:
            if i.isalnum():
                temp+=i
        return temp == temp[::-1]
        


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "]":"[",
            "}":"{",
            ")": "("
        }
        stack =[]

        for i in s:
            if i == "{" or i=="[" or i=="(":
                stack.append(i)
              
            else:
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False
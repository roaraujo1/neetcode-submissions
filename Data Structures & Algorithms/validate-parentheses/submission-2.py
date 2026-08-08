class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack = []

        for i in s:
            if i == "{" or i == "(" or i == "[":
                stack.append(i)
            else:
                if stack:
                    if stack[-1] == pairs[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
            

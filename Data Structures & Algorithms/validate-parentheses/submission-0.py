class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []

        for i in s:
            if i == '[' or i =='(' or i=='{':
                stack.append(i)
            else:
                if not stack:
                    return False
                    
                else:
                    if stack[-1] == pairs.get(i):
                        stack.pop()
                    else:
                        return False
                
        
        if stack:
            return False
        return True

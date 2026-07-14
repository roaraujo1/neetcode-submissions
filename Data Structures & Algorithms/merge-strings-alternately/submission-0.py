class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []
        one,two=0,0

        while one < len(word1) and two < len(word2):
            result.append(word1[one])
            result.append(word2[two])
        
            one+=1
            two+=1

        result.append(word1[one:])
        result.append(word2[two:])
        return "".join(result)
        

    


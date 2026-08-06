class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+= str(len(i))+"*"+i
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        j=0
        res = []
        while i < len(s):
            start = i
            while s[i] != "*":
                i+=1
            j = int(s[start:i])
            res.append(s[i+1:i+1+j])
            i = i+j+1

        return res

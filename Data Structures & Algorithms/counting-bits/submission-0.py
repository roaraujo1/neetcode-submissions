class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)
        for i in range(n+1):
            arr[i] = bin(i).count("1")
        return arr
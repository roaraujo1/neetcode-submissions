import math
import sys
class Solution:
    def numSquares(self, n: int) -> int:
        sys.setrecursionlimit(20000)
        def helper(n,memo):
            if n in memo:
                return memo[n]
            if n==0:
                return 0

            minRes = float("inf")
            for i in range(1,math.floor(math.sqrt(n)+1)):
                square = i*i
                minNum = 1+helper(n-square,memo)
                if minNum < minRes:
                    minRes = minNum
            
            memo[n] = minRes
            return minRes
        return helper(n,{})

            
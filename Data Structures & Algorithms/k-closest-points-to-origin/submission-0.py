import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x,y in points:
            eud = math.sqrt(x**2 + y**2)
            heapq.heappush(heap,(eud,[x,y]))
        
        
        for _ in range(k):
            curr = heapq.heappop(heap)
            res.append(curr[1])
        return res

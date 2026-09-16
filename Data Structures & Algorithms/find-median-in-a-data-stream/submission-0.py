import heapq
class MedianFinder:

    def __init__(self):
        self.max_heapq = []
        self.min_heapq = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heapq, -num)
        heapq.heappush(self.min_heapq, -(heapq.heappop(self.max_heapq)))
        if len(self.min_heapq) - len(self.max_heapq) > 1:
            heapq.heappush(self.max_heapq, -(heapq.heappop(self.min_heapq)))

    def findMedian(self) -> float:
        if len(self.min_heapq) == len(self.max_heapq):
            return (self.min_heapq[0] + -(self.max_heapq[0])) / 2
        else:
            return self.min_heapq[0]
       
        
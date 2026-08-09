class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        
        intervals.sort(key= lambda x : x[0])
        
      
        res = [[intervals[0][0],intervals[0][1]]]
        prevEnd = res[-1][1]


        for start,end in intervals[1:]:
            if prevEnd >= start:
                res[-1] = [min(res[-1][0],start),max(prevEnd,end)]
            else:
                res.append([start,end])
            prevEnd = res[-1][1]
        return res
      
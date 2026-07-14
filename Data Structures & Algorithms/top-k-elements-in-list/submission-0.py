class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = [[] for _ in range(len(nums)+1)]
        
        freq = Counter(nums)
        print(freq)

        for i,v in freq.items():
            cache[v].append(i)
        
        res = []
   
        for i in range(len(cache)-1,-1,-1):
            print(cache[i])
            for j in cache[i]:
                print(j)
                if len(res)==k:
                    return res
                res.append(j)

        return res



     
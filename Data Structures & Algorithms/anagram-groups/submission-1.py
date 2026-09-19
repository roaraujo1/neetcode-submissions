class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for i in strs:
            i_sorted = sorted(i)
            i_join = "".join(i_sorted)
            res[i_join].append(i)

        return list(res.values())
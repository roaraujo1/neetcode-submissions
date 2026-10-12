class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for i in strs:
            i_sorted = sorted(i)
            groups["".join(i_sorted)].append(i)

        return list(groups.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = collections.defaultdict(list)

        for i in strs:
            newWord = "".join(sorted(i))
            matches[newWord].append(i)
        
        return list(matches.values())
        
        

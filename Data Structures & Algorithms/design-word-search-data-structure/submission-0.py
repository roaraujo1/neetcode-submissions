class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(j,curr):
            if j == len(word):
                return curr.is_end
            
            if word[j] == ".":
                for child in curr.children.values():
                    if dfs(j+1,child):
                        return True
                return False
            
            if word[j] not in curr.children:
                return False
            return dfs(j+1,curr.children[word[j]])
        return dfs(0,self.root)
                

        

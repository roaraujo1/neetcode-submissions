class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        visited = set()
        root=self.createTrie(words)
        def backtracking(root, r, c, stringLetters):
            if not (0 <= r < len(board) and 0 <= c < len(board[0])) or (r, c) in visited or board[r][c] not in root.children:
                return
            
            visited.add((r, c))
            node = root.children[board[r][c]]
            stringLetters += board[r][c]
            
            if node.is_end and stringLetters not in res:
                res.append(stringLetters)
            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                backtracking(node, newR, newC, stringLetters)
            visited.remove((r, c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                backtracking(root,r,c,"")
       
        return res
            
            
            

    def createTrie(self,words):
        root = TrieNode()
        curr = root
        for i in words:
            for j in i:
                if j not in curr.children:
                    curr.children[j] = TrieNode()
                curr = curr.children[j]
            curr.is_end = True
            curr = root
        return root
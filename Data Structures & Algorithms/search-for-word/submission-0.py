class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtracking(r,c,ind):
            if ind == len(word):
                return True
            if not(0<= r and r < len(board) and 0<=c and c < len(board[0]) and board[r][c]==word[ind]) or (r,c) in visited:
                return False
            
            visited.add((r,c))
            direction = [(0,1),(1,0),(-1,0),(0,-1)]

            for dr,dc in direction:
                newR,newC = dr+r,dc+c
                if backtracking(newR,newC,ind+1):
                    return True
            
            visited.remove((r,c))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtracking(r,c,0):
                    return True
        
        return False
                

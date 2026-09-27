class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        res = []

        def dfs(r, c, val, ocean):
            if not (0 <= r and r < len(heights) and 0 <= c and c < len(heights[0])) or not (val <= heights[r][c]) or (r, c) in ocean:
                return

            ocean.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                dfs(newR, newC, heights[r][c], ocean)

        ROWS, COLS = len(heights), len(heights[0])

        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row = set()
        zero_col = set()
        

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                if matrix[row][col]==0:
                    zero_row.add(row)
                    zero_col.add(col)

        for i in zero_row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for i in zero_col:
            for j in range(len(matrix)):
                matrix[j][i]=0
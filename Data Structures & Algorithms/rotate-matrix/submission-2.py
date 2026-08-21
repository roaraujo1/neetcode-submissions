class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n//2):
            for j in range(i,n-1-i):
                row,col = i,j

                temp = matrix[row][col]

                matrix[row][col] = matrix[n-1-col][row]
                row,col = n-1-col,row

                matrix[row][col] = matrix[n-1-col][row]
                row,col = n-1-col,row

                matrix[row][col] = matrix[n-1-col][row]
                row,col = n-1-col,row

                matrix[row][col] = temp
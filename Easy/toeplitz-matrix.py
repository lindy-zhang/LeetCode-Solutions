Easy/toeplitz-matrix.py

# Notes:
# - Matrix manipulation
# - Check whether each value is equal to the value of its top left neighbor

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # m = number of rows
        # n = number of columns
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                # If on the top or left edge, move on
                if i == 0 or j == 0:
                    continue
                # Check whether each value is equal to the value of its top left neighbor
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

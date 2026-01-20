Easy/transpose-matrix.py

# Notes:
# - Matrix manipulation

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        new_matrix = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix

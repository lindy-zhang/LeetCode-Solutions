Medium/count-square-submatrices-with-all-ones.py

# Notes:
# - Very similar to Leetcode #221: Maximal Square
# - Dynamic Programming

# O(m*n) 
# Can find faster solution (will update once I solve using O(n)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
      # Logif from #221: Maximal Square
        m, n = len(matrix), len(matrix[0]) # Dimensions of the matrix
        memo = {} # For every pos, store max side length if pos is bottom right
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        memo[(i, j)] = 1
                    else:
                        memo[(i, j)] = min(memo[(i-1, j-1)], memo[i-1, j], memo[(i, j-1)]) + 1
                else: # Can't be square if it's 0
                    memo[(i, j)] = 0
        count = 0
        for i in range(m):
            for j in range(n):
                count += memo[(i, j)]
        return count

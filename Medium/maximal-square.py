Medium/maximal-square.py

# Notes:
# - DP
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        max_side = 0 # Keep track of maximum square side length

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    # Base case: side of the square
                    if i == 0 or j == 0:
                        memo[(i, j)] = 1
                    else:
                        # Look at top, left, and top-left diagonal
                        memo[(i, j)] = min(memo[(i-1, j)], memo[(i, j-1)], memo[(i-1, j-1)]) + 1
                    max_side = max(max_side, memo[(i, j)])
                else:
                    # Can't be a square if it's 0
                    memo[(i, j)] = 0
        return max_side*max_side

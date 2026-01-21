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


# Optimal solution: O(n)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # dp[j] stores the largest square side length ending at the current row, column j
        dp = [0] * n
        total_squares = 0
        prev_diag = 0 # This stores the (i-1, j-1) value
        
        for i in range(m):
            for j in range(n):
                temp = dp[j] # Save the 'above' value before it gets overwritten
                
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[j] = 1
                    else:
                        # dp[j] is 'above', dp[j-1] is 'left', prev_diag is 'diagonal'
                        dp[j] = min(dp[j], dp[j-1], prev_diag) + 1
                    
                    total_squares += dp[j]
                else:
                    dp[j] = 0
                
                # The 'above' value we saved becomes the 'diagonal' for the next column
                prev_diag = temp
                
        return total_squares

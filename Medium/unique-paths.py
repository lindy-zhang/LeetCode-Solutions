Medium/unique-paths.py

# Notes:
# - DP
# - Bottom-up tabulation

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        for i in range(m):
            memo[(i, 0)] = 1
        for j in range(n):
            memo[(0, j)] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                memo[(i, j)] = memo[(i-1, j)] + memo[(i, j-1)]
        
        return memo[(m-1, n-1)]

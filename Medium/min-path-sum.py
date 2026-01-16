Medium/min-path-sum.py

# Notes:
# - DP
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        path_sum = {}
        m, n = len(grid), len(grid[0])
        
        path_sum[(0, 0)] = grid[0][0]
        for i in range(1, m):
            path_sum[(i, 0)] = path_sum[(i-1, 0)] + grid[i][0]
        for j in range(1, n):
            path_sum[(0,j)] = path_sum[(0, j-1)] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                path_sum[(i, j)] = min(path_sum[(i-1, j)], path_sum[(i, j-1)]) + grid[i][j]
        
        return path_sum[(m-1, n-1)]

Medium/unique-paths-ii.py

# Notes:
# - DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # Mark all the obstacles
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    memo[(row, col)] = 0
        # A cell is 1 only if the previous cell was also reachable
        for row in range(len(obstacleGrid)):
            if (row, 0) not in memo:
                memo[(row, 0)] = 1 if row == 0 else memo[(row-1, 0)]
        for col in range(len(obstacleGrid[0])):
            if (0, col) not in memo:
                memo[(0, col)] = 1 if col == 0 else memo[(0, col-1)]
        # Fill in the rest of the grid
        for row in range(1, m):
            for col in range(1, n):
                if (row, col) not in memo:
                    memo[row, col] = memo[row-1, col] + memo[row, col-1]
        return memo[m-1, n-1]

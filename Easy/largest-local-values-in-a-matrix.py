Easy/largest-local-values-in-a-matrix.py

# Notes:
# - Matrix manipulation

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # Generate a (n-2) x (n-2) matrix 
        maxLocal = [[0 for _ in range(n-2)] for _ in range(n-2)]

        # Iterate through every possible top left corner of 3x3 matrix
        for i in range(n-2):
            for j in range(n-2):
                curr_max = 0
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if grid[r][c] > curr_max:
                            curr_max = grid[r][c]
                # Store max value of the 3x3 matrix
                maxLocal[i][j] = curr_max
        return maxLocal

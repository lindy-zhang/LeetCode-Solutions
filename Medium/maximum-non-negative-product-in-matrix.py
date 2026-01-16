Medium/maximum-non-negative-product-in-matrix.py

# Notes:
# - DP
# - pretty similar to min path sum (but must keep track of max and min (most neg) products at every cell
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # Keep track of max positive product, max negative product
        pos_product = {}
        neg_product = {}
        m, n = len(grid), len(grid[0])
        # Base case
        pos_product[(0, 0)], neg_product[(0, 0)] = grid[0][0], grid[0][0]
        # For the first row and column, keep track of the values in both pos_product
        # and neg_product regardless of their sign (since there's only 1 option)
        for i in range(1, m):
            pos_product[(i, 0)] = pos_product[(i-1, 0)]*grid[i][0]
            neg_product[(i, 0)] = neg_product[(i-1, 0)]*grid[i][0]
        for j in range(1, n):
            pos_product[(0, j)] = pos_product[(0, j-1)]*grid[0][j]
            neg_product[(0, j)] = neg_product[(0, j-1)]*grid[0][j]
        # Now fill up the rest of pos_product and neg_product
        for i in range(1, m):
            for j in range(1, n):
                curr = grid[i][j]
                
                # We have 4 candidates for the max/min at this cell:
                # 1. Top Max * curr
                # 2. Top Min * curr
                # 3. Left Max * curr
                # 4. Left Min * curr
                options = [
                    pos_product[(i-1, j)] * curr,
                    neg_product[(i-1, j)] * curr,
                    pos_product[(i, j-1)] * curr,
                    neg_product[(i, j-1)] * curr
                ]
                
                pos_product[(i, j)] = max(options)
                neg_product[(i, j)] = min(options)
        result = pos_product[(m-1, n-1)]
        return result % (10**9 + 7) if result >= 0 else -1

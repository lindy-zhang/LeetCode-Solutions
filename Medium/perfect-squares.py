Medium/perfect-squares.py

# Notes:
# - DP
# - Bottom-up tabulation

class Solution:
    def numSquares(self, n: int) -> int:
        def min_ignore_none(a, b):
            if a is None:
                return b
            if b is None:
                return a
            else:
                return min(a, b)
        
        squares = []
        for i in range(int(math.sqrt(n))):
            squares.append((i+1)**2)

        memo = {}
        # Base case
        memo[0] = 0
        for i in range(1, n+1):
            for square in squares:
                subproblem = i - square
                if subproblem < 0: # ignore when negative
                    continue
                memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)

        return memo[n]

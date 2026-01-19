Medium/combinations.py

# Notes:
# - Recursive backtracking

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []
        
        def backtrack(start):
            # Base case
            if len(sol) == k:
                res.append(sol[:]) # Append a copy of sol to res
                return
            # Iterate from start index to n
            for i in range(start, n+1):
                sol.append(i)
                backtrack(i+1)
                sol.pop()
        
        backtrack(1)
        return res

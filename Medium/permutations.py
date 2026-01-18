Medium/permutations.py

# Notes:
# - Recursive backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res, sol = [], []

        def backtrack():
            # Base case: if length of solution is equal to N
            if len(sol) == N:
                res.append(sol[:])
                return
            # Not at base case
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return res

Medium/subsets.py

# Notes:
# - Recursive backtracking

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res, sol = [], [] # Both start out as empty lists

        def backtrack(i):
            # Base case/leaf node when we're at the end of the array:
            if i == N:
                res.append(sol[:]) # Append a COPY of sol instead of a reference to sol
                return
        
            # Two paths: don't pick nums[i], pick nums[i]

            # 1.) don't pick nums[i]
            backtrack(i+1)

            # 2.) pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res

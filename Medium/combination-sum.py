Medium/combination-sum.py

# Notes:
# - Recursive backtracking

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        
        def backtrack(start, curr_sum):
            # Base Case 1: Success
            if curr_sum == target:
                res.append(sol[:])
                return
            
            # Base Case 2: Exceeded target (Stop searching this branch)
            if curr_sum > target:
                return
            
            for i in range(start, len(candidates)):
                sol.append(candidates[i])
                
                # Pass 'i' instead of 'i + 1' to allow reusing the same element.
                # Also pass the new sum without modifying the variable in the current scope.
                backtrack(i, curr_sum + candidates[i])
                
                # Backtrack: remove the last element to try the next candidate in the loop
                sol.pop()

        backtrack(0, 0)
        return res

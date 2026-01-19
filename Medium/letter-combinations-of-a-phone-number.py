Medium/letter-combinations-of-a-phone-number.py

# Notes:
# - Recursive backtracking

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Map each digits 2-9 to its letters
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}   
        res, sol = [], []

        def backtrack(i):
            # Base case: we've picked a letter for every digit
            if i == len(digits):
                res.append("".join(sol)) # Join the list into a string
                return
            
            # Get the letters for the CURRENT digit only
            current_digit = digits[i]
            for letter in d[current_digit]:
                sol.append(letter)   # 1. Pick
                backtrack(i + 1)      # 2. Explore
                sol.pop()            # 3. Backtrack
        
        backtrack(0)
        return res

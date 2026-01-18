Medium/spiral-matrix.py

# Notes:
# - Matrix/array manipulation

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = [] # This is that array we'll store the spiral ordering in
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1.) Move right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1 # Increment top (move down a row)

            # 2.) Move down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1 # Increment right (move left a column)

            # 3.) Move left (check if row still exists)
            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1 # Increment bottom (move up a row)

            # 4.) Move up (check if col still exists)
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1 # Increment left (move right a row)
        return result

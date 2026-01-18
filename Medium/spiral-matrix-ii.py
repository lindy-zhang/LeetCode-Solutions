Medium/spiral-matrix-ii.py

# Notes:
# - Matrix/array manipulation

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # First let's create the nxn matrix and temporarily fill it with 0s
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, right = 0, n-1
        top, bottom = 0, n-1
        curr_num = 1

        while left <= right and top <= bottom:
            # 1.) Move right
            for i in range(left, right+1):
                matrix[top][i] = curr_num
                curr_num += 1
            top += 1

            # 2.) Move down
            for i in range(top, bottom+1):
                matrix[i][right] = curr_num
                curr_num += 1
            right -= 1

            # 3.) Move left (make sure still in range)
            if left <= right:
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = curr_num
                    curr_num += 1
                bottom -= 1

            # 4.) Move up (make sure still in range)
            if top <= bottom:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = curr_num
                    curr_num += 1
                left += 1
        return matrix

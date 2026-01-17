Medium/triangle.py

# Notes:
# - DP
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        num_rows = len(triangle)
        path_sum = {}
       
        # Base case
        path_sum[(0,0)] = triangle[0][0]
        
        # Fill the far left and far right edges
        for i in range(1, num_rows):
            path_sum[(i, 0)] = path_sum[(i-1, 0)] + triangle[i][0]
            path_sum[(i, i)] = path_sum[(i-1, i-1)] + triangle[i][i]
        
        # Fill the middle elements
        # Start i at 2 because rows 0 and 1 only have "edge" elements
        for i in range(2, num_rows):
            for j in range(1, i):
                path_sum[(i, j)] = min(path_sum[(i-1, j)], path_sum[(i-1, j-1)]) + triangle[i][j]
        
        # Find minimum in last row
        min_path_sum = path_sum[(num_rows-1, 0)]
        for i in range(1, num_rows):
            min_path_sum = min(min_path_sum, path_sum[(num_rows-1, i)])
        return min_path_sum

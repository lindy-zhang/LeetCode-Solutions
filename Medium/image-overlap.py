Medium/image-overlap.py

# Notes:
# - Matrix manipulation

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1) # Size of square matrix (n x n)
        # Extract the position of 1s
        img1_ones = []
        img2_ones = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_ones.append((i, j))
                if img2[i][j] == 1:
                    img2_ones.append((i, j))

        shifts = {} # Dictionary to keep track of the frequency of shifts
        max_count = 0

        for i1, j1 in img1_ones:
            for i2, j2 in img2_ones:
                shift = (i2-i1, j2-j1)
                # If this shift already exists in our dictionary, increment it
                if shift in shifts:
                    shifts[shift] += 1
                else:
                    shifts[shift] = 1
                # Update the maximum # of shifts we've seen so far
                max_count = max(max_count, shifts[shift])
        return max_count

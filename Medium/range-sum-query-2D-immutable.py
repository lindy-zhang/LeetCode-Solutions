Medium/range-sum-query-2D-immutable.py
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        self.pref = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.pref[i+1][j+1] = self.pref[i+1][j] + self.pref[i][j+1] - self.pref[i][j] + matrix[i][j]

        print(self.pref)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Sum = Total area - Top part - Left part + Overlap part
        return (self.pref[row2+1][col2+1] - 
                self.pref[row1][col2+1] - 
                self.pref[row2+1][col1] + 
                self.pref[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

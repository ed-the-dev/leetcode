from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.prefix_matrix: list[list[int]] = [] 

        # Prefix sum along rows

        for row_index in range(0, len(matrix)):
            for column_index in range(0, len(matrix[row_index])):
                prefix: int = matrix[row_index][column_index-1] if column_index > 0 else 0
                matrix[row_index][column_index] = matrix[row_index][column_index] + prefix

        # Now prefix along columns

        for column_index in range (0, len(matrix[0])):
            for row_index in range(0, len(matrix)):
                prefix: int = matrix[row_index-1][column_index] if row_index > 0 else 0
                matrix[row_index][column_index] = matrix[row_index][column_index] + prefix

        self.prefix_matrix = matrix        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:


        # Sum of everything from lower right square
        lower_right: int = self.prefix_matrix[row2][col2]

        # Sum of everything from the one to the left of bottom left to (0,0)
        lhs: int = self.prefix_matrix[row2][col1-1] if col1 > 0 else 0

        # Sum of everything from one above the top right to (0,0)
        top: int = self.prefix_matrix[row1-1][col2] if row1 > 0 else 0

        # Sum of everything one off the top left to (0,0)
        upper_left = self.prefix_matrix[row1-1][col1-1] if min(col1, row1) > 0 else 0

        return lower_right - (lhs+top-upper_left )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
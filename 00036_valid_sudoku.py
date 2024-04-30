from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkGroup(group: list[int]) -> bool:

            valid_set: set[str] = {'1','2','3','4','5','6','7','8','9'}

            for number in group:
                if number == '.':
                    continue
                if number not in valid_set:
                    return False
                else:
                    valid_set.remove(number)
            
            return True
        
        for row in range(0, 3):
            for column in range(0, 3):

                group: list[int] = []

                for inner_row in range(0, 3):
                   for inner_column in range(0,3):
                       row_index = 3*row + inner_row
                       column_index: int = 3*column + inner_column
                       group.append(board[row_index][column_index])

                if not checkGroup(group):
                    return False
                
        for row in range(0, 9):
            group = board[row]

            if not checkGroup(group):
                return False
        
        for column in range(0, 9):
            group: list[int] = []

            for row in range(0, 9):
                group.append(board[row][column])
            
            if not checkGroup(group):
                return False
        
        return True


solution: Solution = Solution()
ham = solution.isValidSudoku(
    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
)

print(ham)

from typing import List
import copy

def isValidSudoku(board: List[List[str]]) -> bool:

    # Write a function that reads in a list and compares it against 

    valid: set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}



    def check_group_valid(group: List[str]) -> bool:

        refreshed_valid = copy.deepcopy(valid)
        for value in group:
            if value == '.':
                continue
            if value in refreshed_valid:
                refreshed_valid.remove(value)
            else:
                return False
        return True

    # Rows

    for row in board:
        row_result: bool = check_group_valid(row)
        if not row_result:
            return False
    
    # Columns

    for i in range (0, 9):
        column: List[str] = []
        for j in range(0, 9):
            column += [board[j][i]]
        
        column_result: bool = check_group_valid(column)
        if not column_result:
            return False
        
    
    # Boxes
        
    for i in range(0, 3):
        for j in range(0, 3):

            # Here in the loop represents the coordinates of each box
            # Work out the 'starting' index of each box.
            # Need to mulitply each index by 3 to work out the starting index.
            starting_x: int = i*3
            starting_y: int = j*3

            group: List[str] = []

            for row_level in range(starting_x, starting_x+3):
                group += board[row_level][starting_y: starting_y+3]

            group_result: bool = check_group_valid(group)
            if not group_result:
                return False
            
    return True

            

    # Make a grid of 3 by 3 to represent the boxes


print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
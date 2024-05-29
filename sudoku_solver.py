# using backtracking search to find sudoku solutions
# here we use an example input, but what if we had a GUI?
# or something that can solve print puzzles from just a picture?

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def find_space(board):
    # find: empty spaces in sudoku grid
    # return: coordinates of empty cell
    for i in range(len(board)): # length 
        for j in range(len(board[0])): # width 
            if board[i][j] == 0:
                return (i, j)

    return None # no empty cells, puzzle is solved

def valid(board, num, cell):
    # check: current assignment is a valid solution
    # return: true or false
    # arguments:
        # board: given sudoku board
        # num: digit from 1-9
        # cell: board position of empty cell

    # check if number is on row or column or square
    
    # rows
    for i in range(len(board[0])):
        if board[cell[0]][i] == num and cell[1] != i: 
            return False

    # columns
    for i in range(len(board)):
        if board[i][cell[1]] == num and cell[0] != i: 
            return False

    # square
    board_x = cell[1] // 3
    board_y = cell[0] // 3

    for i in range(board_y * 3, board_y * 3 + 3):
        for j in range(board_x * 3, board_x * 3 + 3):
            if board[i][j] == num and (i,j) != cell:
                return False

    return True

def solve(board): 
    # do: call other functions to solve the board
    # return: true or false

    # find empty spaces
    empty = find_space(board)

    if not empty:
        return True

    # test every number from 1-9 in empty space
    for i in range(1, 10):
        if valid(board, i, empty):
            board[empty[0]][empty[1]] = i
    
            if solve(board): # keep assigning
                return True # we have a non-empty grid where all placements are valid

            board[empty[0]][empty[1]] = 0 # backtrack

    return False

 
print("Sample Board:")
print(board)

solve(board)

print(" ")
print("Solved Board: ")
print(board)




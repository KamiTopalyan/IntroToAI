import moveCalculator
from copy import copy, deepcopy
'''
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
'''
'''
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
'''


# change as you wish however ensure that the quotes have a space in them
# uppercase is white and lowercase is black
validLetters = ['R', 'N', 'B', 'Q', 'K', 'P', 'r', 'n', 'b', 'q', 'k', 'p', ' ']





#DONE: check if the king is in check
#DONE: check if a piece taking causes a check
#DONE: check if the king can move to a safe place
#DONE: check if the king can be protected 
chess_grid = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', 'P', 'P', 'P', ' ', ' '],
    [' ', ' ', ' ', 'P', 'K', 'P', ' ', ' '],
    [' ', ' ', ' ', 'P', 'P', 'b', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b'], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

# checks if grid is invalid
def invalidGrid(chessGrid, r, c):
    chessGrid[r][c] = '\033[1;32mX'
    chessGrid[r][c+1] = f'\033[0m{chessGrid[r][c+1]}'
    print('\n'.join(' '.join("." if x == " " else str(x) for x in row) for row in chess_grid), "\nInvalid Grid refer to the comment about the grid")

# returns moves for any piece
def getMoves(piece: str, chess_grid, row, col): 
    pieceMoves: dict = {
        'b': [moveCalculator.diagonal_moves],
        'n': [moveCalculator.L_moves],
        'r': [moveCalculator.straight_moves],
        'q': [moveCalculator.straight_moves, moveCalculator.diagonal_moves],
        'p': [moveCalculator.pawn_moves],
        'k': [moveCalculator.king_moves],
        'B': [moveCalculator.diagonal_moves],
        'N': [moveCalculator.L_moves],
        'R': [moveCalculator.straight_moves],
        'Q': [moveCalculator.straight_moves, moveCalculator.diagonal_moves],
        'P': [moveCalculator.pawn_moves],
        'K': [moveCalculator.king_moves]
    }
    return [f(chess_grid, row, col, piece.islower()) for f in pieceMoves[piece]]

# returns a chessbaord with the move inputted
def movePiece(chess_grid, row, col, move):
    test_grid = deepcopy(chess_grid)
    test_grid[move[0]][move[1]] = test_grid[row][col]
    test_grid[row][col] = " "
    return test_grid

# returns the moves that can prevent the check
# TODO: check if the path can be blocked rather than the slot right next to the king
def prevenationMove(piecePos, blockingPos): 
    return [blockingPos, piecePos]


def isChecking(chess_grid):
    for row in range(len(chess_grid)):
        for col in range(len(chess_grid[0])):
            if(not any(value in chess_grid[row][col] for value in validLetters)):
                invalidGrid(chess_grid, row, col)
                break
            
            if(chess_grid[row][col] == " "):
                continue
            
            if(chess_grid[row][col].isupper()): # if the piece is black
                continue

            move_sets = getMoves(chess_grid[row][col], chess_grid, row, col)
            for i in range(len(move_sets)):
                for j in range(len(move_sets[i])):
                    xPos = move_sets[i][j][0]
                    yPos = move_sets[i][j][1]
                    if chess_grid[xPos][yPos] == "K":
                        return {
                            "checkingMove": (xPos , yPos),
                            "check": True,
                            "piece": chess_grid[row][col],
                            "preventationMove": prevenationMove((row, col), (move_sets[i-1][j-1][0], move_sets[i-1][j-1][1])),
                            "piecePos": (row, col)
                        }
                        
    return {
        "checkingMove": (),
        "check": False,
        "piece": "",
        "preventationMove": "",
        "piecePos": ""
    }
# checks if move for the king is safe
def safeKingMove(chess_grid, row, col, move_sets):
    safeMoves = []
    for i in range(len(move_sets)):
        for j in range(len(move_sets[i])):
            new_grid = movePiece(chess_grid, row, col, move_sets[i][j])
            check = isChecking(new_grid)
            if(not check["check"]):
                safeMoves.append(move_sets[i][j])
    return safeMoves
                        
def isPreventable(chess_grid, kingMoved = False):
    isPreventable = False
    check = isChecking(chess_grid)
    if(check["check"] and not kingMoved): # if check is found
        for row in range(len(chess_grid)):
            for col in range(len(chess_grid[0])):
                if(chess_grid[row][col] == " "): # if the piece is empty
                    continue
                if(chess_grid[row][col].islower()): # if the piece is white
                    continue
                
                move_sets = getMoves(chess_grid[row][col], chess_grid, row, col) #  find the moves of the piece that (moves are 2d arrays)
                for i in range(len(move_sets)):
                    for j in range(len(move_sets[i])):
                        if(chess_grid[row][col] == "K" and not kingMoved):
                            if move_sets[i][j] == check["piecePos"]: # if the king can take the piece
                                new_grid = movePiece(chess_grid, row, col, move_sets[i][j])
                                kingMoved = True
                                test_check = isChecking(new_grid)
                                if(not test_check["check"]):
                                    isPreventable = True
                            else: # if the king cant take a piece
                                kingMoved = True
                                if(len(safeKingMove(chess_grid, row, col, move_sets)) > 0): # if the king can move to a safe place
                                    for count, safeMove in enumerate(safeKingMove(chess_grid, row, col, move_sets)): # print the outcomes
                                        new_grid = movePiece(chess_grid, row, col, safeMove)
                                        print('\n'.join(' '.join("." if x == " " else str(x) for x in row) for row in new_grid), f"\nMove {count}\n")
                                    isPreventable = True
                        
                        elif move_sets[i][j] in check["preventationMove"] and move_sets[i][j] != check["checkingMove"]: # if the piece can take the checking piece or block it
                            new_grid = movePiece(chess_grid, row, col, safeMove)
                            test_check = isChecking(new_grid)
                            if(not test_check["check"]):
                                print('\n'.join(' '.join("." if x == " " else str(x) for x in row) for row in new_grid))
                                print()
                                isPreventable = True
                            continue
    return isPreventable
def isCheckmate(chess_grid):
    if(not isChecking(chess_grid)["check"]):
        return False
    if(isPreventable(chess_grid)):
        return False
    return True
print(isCheckmate(chess_grid))
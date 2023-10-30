import moveCalculator
from copy import deepcopy
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
    [' ', ' ', ' ', 'P', 'P', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', 'R', ' ', 'b'], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

def printGrid(chess_grid, textToAppend):
    print('\n'.join(' '.join("." if x == " " else str(x) for x in row) for row in chess_grid), textToAppend)

# checks if grid is invalid
def invalidGrid(chess_grid: list[list[str]], r: int, c: int) -> None:
    chess_grid[r][c] = '\033[1;32mX'
    chess_grid[r][c+1] = f'\033[0m{chess_grid[r][c+1]}'
    printGrid(chess_grid, "\nInvalid Grid refer to the comment about the grid")

# returns moves for any piece
def getMoves(piece: str, chess_grid: list[list[validLetters]], row: int, col: int) -> list[tuple[int, int]]: 
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
def movePiece(chess_grid: list[list[str]], row: int, col: int, move: tuple[int, int]) -> list[list[str]]:
    test_grid = deepcopy(chess_grid)
    test_grid[move[0]][move[1]] = test_grid[row][col]
    test_grid[row][col] = " "
    return test_grid

# returns the moves that can prevent the check
# DONE: check if the path can be blocked rather than the slot right next to the king
def prevenationMoves(piecePos: tuple, blockingPos: tuple) -> list[tuple[int, int]]: 
    return [blockingPos, piecePos]


def isChecking(chess_grid: list[list[str]]) -> dict:
    for row in range(len(chess_grid)):
        for col in range(len(chess_grid[0])):
            if(chess_grid[row][col] == " "):
                continue
            
            if(chess_grid[row][col].isupper()): # if the piece is black
                continue

            move_sets = getMoves(chess_grid[row][col], chess_grid, row, col)
            for i in range(len(move_sets)):
                for j in range(len(move_sets[i])):
                    for k in range(len(move_sets[i][j])):
                        xPos = move_sets[i][j][k][0]
                        yPos = move_sets[i][j][k][1]
                        if chess_grid[xPos][yPos] == "K":
                            move_sets[i][j].append((row, col))
                            return {
                                "checkingMove": (xPos , yPos),
                                "check": True,
                                "piece": chess_grid[row][col],
                                "preventationMove": move_sets[i][j],
                                "piecePos": (row, col)
                            }
    # if no check is found          
    return {
        "checkingMove": (),
        "check": False,
        "piece": "",
        "preventationMove": "",
        "piecePos": ""
    }

"""
    This function takes in a chess grid, a row, a column, and a list of moves, and returns
    a list of safe moves for the king. For every possible move for the king, it creates a
    new grid and checks to see if the king is in check in the new grid. If the king is not
    in check, the move is added to the list of safe moves. The function returns the list of
    safe moves.
"""
def safeKingMove(chess_grid: list[list[str]], row: int, col: int, move_sets: list[list[tuple[int, int]]]) -> list[tuple[int, int]]:
    safeMoves = []
    for i in range(len(move_sets)):
        for j in range(len(move_sets[i])):
            for k in range(len(move_sets[i][j])):
                new_grid = movePiece(chess_grid, row, col, move_sets[i][j][k])
                check = isChecking(new_grid)
                if(not check["check"]):
                    safeMoves.append(move_sets[i][j][k])
    return safeMoves
                        
def isPreventable(chess_grid: list[list[str]], kingMoved: bool = False) -> bool:
    isPreventable = False
    check = isChecking(chess_grid)
    if(check["check"] and not kingMoved): # if check is found
        for row in range(len(chess_grid)):
            for col in range(len(chess_grid[0])):
                if(chess_grid[row][col] == " "): # if the piece is empty
                    continue
                if(chess_grid[row][col].islower()): # if the piece is white
                    continue
                #  find the moves of the piece 
                # (moves are 3d arrays move type, move direction, move position)
                move_sets = getMoves(chess_grid[row][col], chess_grid, row, col) 
                for i in range(len(move_sets)):
                    for j in range(len(move_sets[i])):
                        for k in range(len(move_sets[i][j])):
                            # if the piece is the king and if the king has not moved
                            if(chess_grid[row][col] == "K" and not kingMoved):
                                # if the king can take the piece
                                if move_sets[i][j] == check["piecePos"]:
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
                                            printGrid(new_grid, f"\nMove {count}\n")
                                        isPreventable = True
                            # if the piece can take the checking piece or block it
                                
                            elif move_sets[i][j][k] in check["preventationMove"] and move_sets[i][j][k] != check["checkingMove"]: 
                                new_grid = movePiece(chess_grid, row, col, move_sets[i][j][k])
                                test_check = isChecking(new_grid)
                                if(not test_check["check"]):
                                    printGrid(new_grid, "\n")
                                    isPreventable = True
                                continue
    return isPreventable

def isCheckmate(chess_grid):
    # if the grid is invalid as in letter are not in the validLetters list
    for row in range(len(chess_grid)):
        for col in range(len(chess_grid[0])):
            if(not any(value in chess_grid[row][col] for value in validLetters)): 
                invalidGrid(chess_grid, row, col)
                exit(0)
    if(not isChecking(chess_grid)["check"]):
        return False
    if(isPreventable(chess_grid)):
        return False
    return True

print(isCheckmate(chess_grid))
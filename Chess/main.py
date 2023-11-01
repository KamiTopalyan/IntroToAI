from itertools import product
import moveCalculator
from copy import deepcopy
import time
import os, psutil
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
#DONE: check if the path can be blocked rather than the slot right next to the king
chess_grid = [
    [' ', ' ', 'P', 'K', ' ', ' ', ' ', 'r'],
    [' ', ' ', 'P', 'P', 'P', 'n', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', 'R', 'R', ' ', ' ', ' ']
]

def printGrid(chess_grid, textToAppend):
    print('\n'.join(' '.join("." if x == " " else str(x) for x in row) for row in chess_grid), textToAppend)

# checks if grid is invalid
def invalidGrid(chess_grid: list[list[str]], r: int, c: int) -> None:
    chess_grid[r][c] = '\033[1;32mX' # Color format to make x green
    chess_grid[r][c+1] = f'\033[0m{chess_grid[r][c+1]}' # color format to reset the color
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

# returns a chessboard with the move inputted
def movePiece(chess_grid: list[list[str]], row: int, col: int, move: tuple[int, int]) -> list[list[str]]:
    test_grid = deepcopy(chess_grid)
    test_grid[move[0]][move[1]] = test_grid[row][col]
    test_grid[row][col] = " "
    return test_grid

def isChecking(chess_grid: list[list[str]]) -> dict:
    for row, col in product(range(len(chess_grid)), range(len(chess_grid[0]))):
        if(chess_grid[row][col] == " "):
            continue
        
        if(chess_grid[row][col].isupper()): # if the piece is black
            continue

        move_sets = getMoves(chess_grid[row][col], chess_grid, row, col)
        for moveType in range(len(move_sets)):
            for movePath in range(len(move_sets[moveType])):
                for movePosition in range(len(move_sets[moveType][movePath])):
                    xPos, yPos = move_sets[moveType][movePath][movePosition][0],move_sets[moveType][movePath][movePosition][1]
                    if chess_grid[xPos][yPos] == "K":
                        move_sets[moveType][movePath].append((row, col))
                        return {
                            "checkingMove": (xPos , yPos),
                            "check": True,
                            "piece": chess_grid[row][col],
                            "preventationMove": move_sets[moveType][movePath],
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
    for moveType in range(len(move_sets)):
        for movePath in range(len(move_sets[moveType])):
            for movePosition in range(len(move_sets[moveType][movePath])):
                new_grid = movePiece(chess_grid, row, col, move_sets[moveType][movePath][movePosition])
                check = isChecking(new_grid)
                if(not check["check"]):
                    safeMoves.append(move_sets[moveType][movePath][movePosition])
    return safeMoves
                        
def isPreventable(chess_grid: list[list[str]], kingMoved: bool = False) -> bool:
    isPreventable = False
    check = isChecking(chess_grid)
    if(kingMoved): return isPreventable
    for row, col in product(range(len(chess_grid)), range(len(chess_grid[0]))):
        if(chess_grid[row][col] == " "): # if the piece is empty
            continue
        
        if(chess_grid[row][col].islower()): # if the piece is white
            continue
        
        #  find the moves of the piece 
        # (moves are 3d arrays move type, move path, move position)
        move_sets = getMoves(chess_grid[row][col], chess_grid, row, col)
        for moveType in range(len(move_sets)):
            for movePath in range(len(move_sets[moveType])):
                for movePosition in range(len(move_sets[moveType][movePath])):
                    currentMove = move_sets[moveType][movePath][movePosition]
                    if(chess_grid[row][col] == "K" and not kingMoved):
                        # if the king can take the piece
                        if move_sets[moveType][movePath] == check["piecePos"]:
                            new_grid = movePiece(chess_grid, row, col, move_sets[moveType][movePath])
                            kingMoved = True
                            test_check = isChecking(new_grid)
                            if(not test_check["check"]):
                                isPreventable = True
                        else: # if the king cant take a piece
                            kingMoved = True
                            # if the king can move to a safe place
                            if(len(safeKingMove(chess_grid, row, col, move_sets)) > 0): 
                                isPreventable = True
                                # print the outcomes
                                for count, safeMove in enumerate(safeKingMove(chess_grid, row, col, move_sets)): 
                                    new_grid = movePiece(chess_grid, row, col, safeMove)
                                    printGrid(new_grid, f"\nMove {count}\n")
                                
                    # if the piece can take the checking piece or block it
                    elif (currentMove in check["preventationMove"] and currentMove != check["checkingMove"]): 
                        new_grid = movePiece(chess_grid, row, col, currentMove)
                        test_check = isChecking(new_grid)
                        if not test_check["check"] :
                            printGrid(new_grid, "\n")
                            isPreventable = True
    return isPreventable

def isCheckmate(chess_grid):
    # if the grid is invalid as in letter are not in the validLetters list
    for row, col in product(range(len(chess_grid)), range(len(chess_grid[0]))):
        if(not any(value in chess_grid[row][col] for value in validLetters)): 
            invalidGrid(chess_grid, row, col)
            exit(0)

    if not isChecking(chess_grid)["check"] :
        return False

    if isPreventable(chess_grid):
        return False
    
    return True

if(__name__ == "__main__"):
    process = psutil.Process()
    st = time.time()
    result = isCheckmate(chess_grid)
    et = time.time()
    print(f"Checkmate: {result}\nTime to calculate: {round(((et - st) * 1000), 5)}ms\nMemory: {process.memory_info().rss / 1024 / 1000} MB")
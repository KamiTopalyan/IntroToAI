
# @returns a 2d list of all the possible moves for a bishop
def diagonal_moves(chess_grid, row, col, isWhite):
    moves = []
    
    # Check diagonal up-right
    r, c = row - 1, col + 1
    while r >= 0 and c < len(chess_grid[0]):
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper() if isWhite else chess_grid[r][c].islower():
            moves.append((r, c))
            break
        else:
            break
        r -= 1
        c += 1
        
    # Check diagonal up-left
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper() if isWhite else chess_grid[r][c].islower():
            moves.append((r, c))
            break
        else:
            break
        r -= 1
        c -= 1
        
    # Check diagonal down-right
    r, c = row + 1, col + 1
    while r < len(chess_grid) and c < len(chess_grid[0]):
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper() if isWhite else chess_grid[r][c].islower():
            moves.append((r, c))
            break
        else:
            break
        r += 1
        c += 1
        
    # Check diagonal down-left
    r, c = row + 1, col - 1
    while r < len(chess_grid) and c >= 0:
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper() if isWhite else chess_grid[r][c].islower():
            moves.append((r, c))
            break
        else:
            break
        r += 1
        c -= 1
    return moves

def straight_moves(chess_grid, row, col, isWhite):
    moves = []
    
    #Moves to the right
    r, c = row, col + 1
    while c < len(chess_grid[0]):
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper() if isWhite else chess_grid[r][c].islower():
            moves.append((r, c))
            break
        else:
            break
        c += 1
        
    #Moves to the left
    r, c = row, col - 1
    while c > 0:
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper() if isWhite else chess_grid[r][c].islower():
            moves.append((r, c))
            break
        else:
            break
        c -= 1
    
    #Moves to up
    r, c = row - 1, col  
    while r > 0:
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper() if isWhite else chess_grid[r][c].islower():
            moves.append((r, c))
            break
        else:
            break
        r -= 1

    #Moves to down
    r, c = row + 1, col  
    while r < len(chess_grid[0]):
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper() if isWhite else chess_grid[r][c].islower():
            moves.append((r, c))
            break
        else:
            break
        r += 1
    return moves

def L_moves(chess_grid, row, col, isWhite):
    moves = []
    offsets = [
                (2, 1), (1, 2),
                (-2, -1), (-1, -2),
                (-2, 1), (-1, 2),
                (2, -1), (1, -2)
               ]
    for move in offsets:
        rOffset, cOffset = move[0] + row, move[1] + col
        if(rOffset < 0 or rOffset >= len(chess_grid)):
            continue
        if(cOffset < 0 or cOffset >= len(chess_grid[0])):
            continue
        
        if chess_grid[rOffset][cOffset] == ' ': #if no enemy
            moves.append((rOffset, cOffset))
        elif chess_grid[rOffset][cOffset].isupper(): # if enemy found
            moves.append((rOffset, cOffset))

    return moves

def pawn_moves(chess_grid, row, col, isWhite):
    moves = []
    if(isWhite):
        if(row == 0): return moves
        if(row == 6 and chess_grid[row - 1][col] == " " and chess_grid[row - 2][col] == " "): moves.append((row-2,col))

        if (col < len(chess_grid[0]) -1  and chess_grid[row - 1][col + 1].isupper()): moves.append((row-1,col+1)) #to the right
        if (col >= 0 and chess_grid[row - 1][col - 1].isupper()): moves.append((row-1,col-1))# to the left
        if chess_grid[row - 1][col] == " ": moves.append((row-1,col))

    else:
        if(row == 8): return moves
        if(row == 1 and chess_grid[row + 1][col] == " " and chess_grid[row + 2][col] == " "): moves.append((row+2,col))

        if (col < len(chess_grid[0]) - 1  and chess_grid[row + 1][col + 1].islower()): moves.append((row+1,col+1)) #to the right
        if (col >= 0 and chess_grid[row + 1][col - 1].islower()): moves.append((row+1,col-1))# to the left
        if chess_grid[row + 1][col] == " ": moves.append((row+1,col))

    return moves

def king_moves(chess_grid, row, col, isWhite):
    moves = []
    for r in range(-1,2):
        for c in range(-1,2):
            rOffset, cOffset = r + row, c + col
            if(rOffset < 0 or rOffset >= len(chess_grid)):
                continue
            if(cOffset < 0 or cOffset >= len(chess_grid[0])):
                continue
            if r == 0 and c == 0: continue
            if chess_grid[rOffset][cOffset] == " ": moves.append((rOffset, cOffset))
            elif chess_grid[rOffset][cOffset].isupper() if isWhite else chess_grid[rOffset][cOffset].islower(): moves.append((rOffset, cOffset))
    return moves
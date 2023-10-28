
# @returns a 2d list of all the possible moves for a bishop
def diagonal_moves(chess_grid, row, col):
    moves = []
    
    # Check diagonal up-right
    r, c = row - 1, col + 1
    while r >= 0 and c < len(chess_grid[0]):
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper():
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
        elif chess_grid[r][c].isupper():
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
        elif chess_grid[r][c].isupper():
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
        elif chess_grid[r][c].isupper():
            moves.append((r, c))
            break
        else:
            break
        r += 1
        c -= 1
    return moves

def straight_moves(chess_grid, row, col):
    moves = []
    
    #Moves to the right
    r, c = row, col + 1
    while c < len(chess_grid[0]):
        if chess_grid[r][c] == ' ':
            moves.append((r, c))
        elif chess_grid[r][c].isupper():
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
        elif chess_grid[r][c].isupper():
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
        elif chess_grid[r][c].isupper():
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
        elif chess_grid[r][c].isupper():
            moves.append((r, c))
            break
        else:
            break
        r += 1
    return moves

def L_moves(chess_grid, row, col):
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

def pawn_moves(chess_grid, row, col):
    moves = []
    if(row == 0): return moves
    if(row == 6): moves.append((2,0))
    if (col < len(chess_grid[0]) and chess_grid[row + 1][col + 1].isupper()): moves.append((1,1))
    if (chess_grid[row + 1][col - 1].isupper() and col > 0): moves.append((1,-1))
    if chess_grid[row + 1][col] == " ": moves.append((1,0))
    print(moves)
    return moves
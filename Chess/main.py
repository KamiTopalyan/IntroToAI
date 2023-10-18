
# @returns a 2d list of all the possible moves for a bishop
def bishop_moves(chess_grid, row, col):
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

chess_grid = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
    [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
    ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
    [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
    ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]

for row in range(len(chess_grid)):
    for col in range(len(chess_grid[0])):
        if chess_grid[row][col] == 'b':
            moves = bishop_moves(chess_grid, row, col)
            for move in moves:
                print(moves)
                if chess_grid[move[0]][move[1]] == 'K':
                    print("The white bishop is checking the black king!")
                    break

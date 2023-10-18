
# @returns a 2d list of all the possible moves for a bishop
def bishop_moves(chess_grid, row, col):
    moves = []
    
    # Check diagonal up-right
    i, j = row - 1, col + 1
    while i >= 0 and j < len(chess_grid[0]):
        if chess_grid[i][j] == ' ':
            moves.append((i, j))
        elif chess_grid[i][j].isupper():
            moves.append((i, j))
            break
        else:
            break
        i -= 1
        j += 1
        
    # Check diagonal up-left
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if chess_grid[i][j] == ' ':
            moves.append((i, j))
        elif chess_grid[i][j].isupper():
            moves.append((i, j))
            break
        else:
            break
        i -= 1
        j -= 1
        
    # Check diagonal down-right
    i, j = row + 1, col + 1
    while i < len(chess_grid) and j < len(chess_grid[0]):
        if chess_grid[i][j] == ' ':
            moves.append((i, j))
        elif chess_grid[i][j].isupper():
            moves.append((i, j))
            break
        else:
            break
        i += 1
        j += 1
        
    # Check diagonal down-left
    i, j = row + 1, col - 1
    while i < len(chess_grid) and j >= 0:
        if chess_grid[i][j] == ' ':
            moves.append((i, j))
        elif chess_grid[i][j].isupper():
            moves.append((i, j))
            break
        else:
            break
        i += 1
        j -= 1
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

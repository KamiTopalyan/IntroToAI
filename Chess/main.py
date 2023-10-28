import moveCalculator

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

# change as you wish however ensure that the quotes have a space in them
# uppercase is white and lowercase is black
validLetters = ['R', 'N', 'B', 'Q', 'K', 'P', 'r', 'n', 'b', 'q', 'k', 'p', ' ']
chess_grid = [
    ['R', 'N', 'B', 'Q', ' ', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
    [' ', ' ', ' ', ' ', 'r', ' ', 'K', ' '],
    [' ', ' ', ' ', ' ', ' ', 'q', ' ', 'p'],
    [' ', ' ', ' ', ' ', ' ', 'n', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', ' ', 'p', 'p', 'p', 'p'], 
    ['r', ' ', ' ', ' ', 'k', 'b', ' ', 'r']
]

def invalidGrid(chessGrid, r, c):
    chessGrid[r][c] = '\033[1;32mX'
    chessGrid[r][c+1] = f'\033[0m{chessGrid[r][c+1]}'
    print('\n'.join(' '.join("." if x == " " else str(x) for x in row) for row in chess_grid), "\nInvalid Grid refer to the comment about the grid")

for row in range(len(chess_grid)):
    for col in range(len(chess_grid[0])):
        if(not any(value in chess_grid[row][col] for value in validLetters)):
            invalidGrid(chess_grid, row, col)
            break
        if chess_grid[row][col] == 'b':
            move_sets = []
            move_sets.append(moveCalculator.diagonal_moves(chess_grid, row, col))
            for sets in move_sets:
                for move in sets:
                    if chess_grid[move[0]][move[1]] == 'K':
                        print("The white bishop is checking the black king!")
                        break
        elif chess_grid[row][col] == 'n':
            move_sets = []
            move_sets.append(moveCalculator.L_moves(chess_grid, row, col))
            for sets in move_sets:
                for move in sets:
                    if chess_grid[move[0]][move[1]] == 'K':
                        print("The white knight is checking the black king!")
                        break
        elif chess_grid[row][col] == 'r':
            move_sets = []
            move_sets.append(moveCalculator.straight_moves(chess_grid, row, col))
            for sets in move_sets:
                for move in sets:
                    if chess_grid[move[0]][move[1]] == 'K':
                        print("The white rook is checking the black king!")
                        break
        elif chess_grid[row][col] == 'q':
            move_sets = []
            move_sets.append(moveCalculator.straight_moves(chess_grid, row, col))
            move_sets.append(moveCalculator.diagonal_moves(chess_grid, row, col))
            for sets in move_sets:
                for move in sets:
                    if chess_grid[move[0]][move[1]] == 'K':
                        print("The white queen is checking the black king!")
                        break
        elif chess_grid[row][col] == 'p':
            move_sets = []
            move_sets.append(moveCalculator.pawn_moves(chess_grid, row, col))
            for sets in move_sets:
                for move in sets:
                    if chess_grid[move[0]][move[1]] == 'K':
                        print("The white pawn is checking the black king!")
                        break
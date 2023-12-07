from Tree import Tree
from Grid import Grid
from time import sleep

grid = Grid()
grid.read("Berkeley/layouts/bigMaze.lay")

def lookAround(Grid: Grid, slot: Grid.GridSlot, visited: list[tuple]) -> None:
    x = slot.key[0]
    y = slot.key[1]
    moves = []
    if(not Grid.isWall(x+1,y) and (x+1,y) not in visited):
        moves.append((x+1,y))
    if(not Grid.isWall(x-1,y) and (x-1,y) not in visited):
        moves.append((x-1,y))
    if(not Grid.isWall(x,y-1) and (x,y-1) not in visited):
        moves.append((x,y-1) )
    if(not Grid.isWall(x,y+1) and (x,y+1) not in visited):
        moves.append((x,y+1))
    
    return moves

def generateTree(Grid: Grid, startPos):
    tree = Tree()
    root = tree.newNode(startPos)
    visited = []
    moves = lookAround(Grid, root, visited)
    visited.append(startPos)
    queue = [root]
    while len(queue) > 0:
        root = queue.pop(0) 
        moves = lookAround(Grid, root, visited)
        for move in moves:
            node = tree.generateAndAppend(root, move)
            queue.append(node)
            print(Grid.getFinalGrid(tree, visited))
            sleep(0.0005)
            if Grid.isTarget(move[1], move[0]):
                print("Found")
                return tree
            visited.append(move)

generateTree(grid, grid.startPos)

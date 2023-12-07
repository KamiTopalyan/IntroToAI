import Maze_Reader as reader
from Tree import Grid, Tree
from time import sleep
Grid2 = Grid()
reader.read(Grid2)

def lookAround(Grid: Grid, slot, visited) -> None:
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
            visited.append(move)
            print(Grid.getGridWithPos(move))
            sleep(0.1)
            if Grid.isTarget(move[1], move[0]):
                print("Found")
                return
            

generateTree(Grid2, Grid2.startPos)

from Tree import Tree
from Grid import Grid
from time import sleep
import sys
grid1 = Grid()
grid1.read("Berkeley/layouts/mediumMaze.lay")

def lookAround(Grid: Grid, slot: Grid.GridSlot, visited: list[tuple]) -> list[tuple]:
    x = slot.key[0]
    y = slot.key[1]
    moves = []
    try:
        if(not Grid.isWall(x+1,y) and (x+1,y) not in visited):
            moves.append((x+1,y)) # right
        if(not Grid.isWall(x-1,y) and (x-1,y) not in visited):
            moves.append((x-1,y)) # left
        if(not Grid.isWall(x,y-1) and (x,y-1) not in visited):
            moves.append((x,y-1) ) # up
        if(not Grid.isWall(x,y+1) and (x,y+1) not in visited):
            moves.append((x,y+1)) # down
    except IndexError:
        pass
    return moves 

def generateTreeBFS(Grid: Grid, startPos: tuple):
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
            sleep(0.0000001)
            if Grid.isTarget(move[1], move[0]):
                print("Found")
                return tree
            visited.append(move)
    print(Grid.getFinalGrid(tree, visited))
def DFS(Tree: Tree, Grid: Grid, startPos: tuple, root: Tree.Node, moves: list[tuple], visited: set[tuple], found: bool):
    if (root == None):
        sys.exit()

    neighbors = []
    moves = lookAround(Grid, root, visited)
    for move in moves:
        neighbors.append(Tree.Node(move))
    visited.add(root.key)
    for neighbor in neighbors:
        sleep(0.0001)
        visited.add(root.key)
        if(Grid.isTarget(neighbor.key[1], neighbor.key[0])):
            found = True
            print(Grid.getFinalGrid(Tree, visited))
            print("Found")
            sys.exit()
        
        print(Grid.getFinalGrid(Tree, visited))
        DFS(Tree, Grid, startPos, neighbor, moves, visited, found)
    print(Grid.getFinalGrid(Tree, visited))
        
found = False
tree = Tree()
#DFS(tree, grid1, grid1.startPos, tree.newNode(grid1.startPos), [], set(),found)
generateTreeBFS(grid1, grid1.startPos)
'''
    A
   / \ 
  C   D
 / \ / \
E   F   G
   / \
  H   I
  
A -> C -> E -> C -> F -> H -> I -> A -> D -> G

while len(temp)!=0 and temp not in visited
visited.append(temp)
temp = temp[n]      OUT OF BOUNDS?

queue = [A]
visited = set()
while len(queue) > 0:
    node = queue.pop()
    if node not in visited:
        visited.add(node)
        moves = lookAround(node)
        for move in moves:
            tree.appendNode(node, move)
            
A -> C 
'''

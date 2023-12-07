
    
class Tree:
    class Node:
        def __init__(self, key, depth = 0, data: dict = None):
            self.key = key
            self.childeren = []
            self.depth = depth
            self.marked = False
            self.data = data
        def getKey(self):
            return self.key

    def newNode(self, key, depth = 0, data: dict = None):    
        return self.Node(key, depth, data)

    def append(self, parentNode: Node, node: Node):
        node.depth = parentNode.depth + 1
        parentNode.childeren.append(node)
        return node
    
    def generateAndAppend(self, parentNode: Node, key, data: dict = None):
        node = self.newNode(key, parentNode.depth + 1, data)
        parentNode.childeren.append(node)
        return node
    
    def DFS(self, root: Node):
        if (root == None):
            return;
        
        root.marked = True
        print(f"{root.key}", end=' ')
        
        for child in root.childeren:
            if (child.marked == False):
                self.DFS(child)
                
    def BFS(self, root: Node):
        if (root == None):
            return;
    
        # using queue
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            if node.marked:
                return
            
            node.marked = True
            print(f"{node.key}", end=' ')
            for child in node.childeren:
                if not child.marked:
                    q.append(child)
                    
                        
            
    def printTree(self, root: Node):
        if (root == None):
            return;
    
        q = []  # Create a queue
        q.append(root); # Enqueue root 
        while (len(q) != 0):
        
            n = len(q);
    
            # If this node has children
            while (n > 0):
                p = q[0]
                q.pop(0);
                print(f"{p.key}, Marked: {p.marked}", end=' ')
                p.marked = False
                # Enqueue all children of the dequeued item
                for i in range(len(p.childeren)):
                
                    q.append(p.childeren[i]);
                    
                n -= 1
    
            print() # Print new line between two levels
class Grid:
    GridVar = []
    startPos = 0
    targetPos = 0
    class GridSlot:
        def __init__(self, x, y, iswall, value):
            self.pos = (x,y)
            self.iswall = iswall
            self.value = value
    def setStartPos(self, pos):
        self.startPos = pos
        
    def setTargetPos(self, pos):
        self.targetPos = pos
        
    def append(self, x, y, iswall, index, value):
        self.GridVar[index].append(self.GridSlot(x,y,iswall, value))
        
    def generateRow(self, count):
        for _ in range(count):
            self.GridVar.append([])
            
    def getGrid(self):
        return self.GridVar
    
    def isWall(self, x, y):
        return self.GridVar[y][x].iswall
    
    def isTarget(self, x, y):
        return self.targetPos == (x,y)
    def getGridWithPos(self, pos):
        string = ""
        for x in range(len(self.GridVar)):
            for y in range(len(self.GridVar[x])):
                string += f"{'X' if (x == pos[1] and y == pos[0]) else self.GridVar[x][y].value}"
            string += "\n"
        return string
    
    def __str__(self):
        string = ""
        for x in range(len(self.GridVar)):
            for y in range(len(self.GridVar[x])):
                string += f"{'%' if self.GridVar[x][y].iswall else ' '}"
            string += "\n"
        return string
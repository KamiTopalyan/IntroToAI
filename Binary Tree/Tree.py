class Node:
    def __init__(self, key, depth = 0, data: dict = None):
        self.key = key
        self.childeren = []
        self.depth = depth
        self.marked = False
        self.data = data
    
        
   
class Tree:
    def newNode(self, key, depth = 0, data: dict = None):    
        return Node(key, depth, data)

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
            if not node.marked:
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
            
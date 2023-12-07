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
        
    def DFSwithStack(self, root: Node):
        if (root == None):
            return;
        
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node.marked:
                return
            
            node.marked = True
            print(f"{node.key}", end=' ')
            for child in node.childeren:
                if not child.marked:
                    stack.append(child)
    def BFS(self, root: Node):
        if (root == None):
            return;

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
                    
                        
            

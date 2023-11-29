from Tree import Tree, Node

Tree = Tree()
root = Tree.newNode(0);

Node1 = Tree.append(root, Tree.newNode(1))
Node2 = Tree.append(root, Tree.newNode(2))
Node3 = Tree.append(Node1, Tree.newNode(3))
Node4 = Tree.append(Node1, Tree.newNode(4))
Node5 = Tree.append(Node2, Tree.newNode(5))
Node6 = Tree.append(Node2, Tree.newNode(6))
Tree.printTree(root)

print()


Tree.BFS(root)
print()
Tree.printTree(root)
print()

Tree.DFS(root)
print()
Tree.printTree(root)
print()

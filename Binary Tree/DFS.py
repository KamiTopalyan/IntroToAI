from Tree import Tree

GeneralTree = Tree()
root: Tree.Node = GeneralTree.newNode(0)

Node1 = GeneralTree.append(root, GeneralTree.newNode(1))
Node2 = GeneralTree.append(root, GeneralTree.newNode(2))
Node3 = GeneralTree.append(Node1, GeneralTree.newNode(3))
Node4 = GeneralTree.append(Node1, GeneralTree.newNode(4))
Node5 = GeneralTree.append(Node2, GeneralTree.newNode(5))
Node6 = GeneralTree.append(Node2, GeneralTree.newNode(6))
GeneralTree.append(Node2, root)
print()


GeneralTree.DFSwithStack(root)
print()

'''
    0
   /  \ 
  1    2
 / \  / \
3  4 5   6
'''
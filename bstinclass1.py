class Node:
  def __init__(self,data):
    self.data = data
    self.right = None
    self.left = None
class BST:
  def __init__(self):
    self.root = None 

  def add_data(self, data):
    self.root = self.add_data_recursive(self.root, data)
  def add_data_recursive(self, node, data):
    if node is None:
      return Node(data)
    if data < node.data:
      node.left = self.add_data_recursive(node.left, data)
    elif data > node.data:
      node.right = self.add_data_recursive(node.right, data)
    return node
  def preorder(self):
    self.preorderrecursive(self.root)
    print()
  def preorderrecursive(self, node):
    if node:
      print(node.data, end=' ')
      self.preorderrecursive(node.left)
      self.preorderrecursive(node.right)

bst = BST()
bst.add_data(30)
bst.add_data(20)
bst.add_data(40)
bst.add_data(60)
bst.add_data(80)
bst.add_data(100)
bst.preorder()

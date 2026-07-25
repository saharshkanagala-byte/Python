#bst : binary search tree is a type of binary tree data structure in which each node contains a unique key that satisfies a specific oredering property: 
#all nodes in left sub tree of a node contains values strictly less than the node's value.
#all nodes in the right sub tree of a node contains values strictly greater than the node's value.
#this structre enables efficient operation for searching insertion and deletion of any elements specially when the tree remains balanced.


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None
  #insertion
  def insert(self, data):
    self.root = self.insertrecursive(self.root , data)
  def insertrecursive(self, node, data):
    if node is None:
      return Node(data)
    if data < node.data:
      node.left = self.insertrecursive(node.left, data)
    elif data > node.data:
      node.right = self.insertrecursive(node.right, data)
    return node      
  def inorder(self):
    self.inorderrecursive(self.root)     
    print()
  def inorderrecursive(self, node):
    if node:
      self.inorderrecursive(node.left)
      print(node.data, end=' ')
      self.inorderrecursive(node.right)
  def preorder(self):
    self.preorderrecursive(self.root)
    print()
  def preorderrecursive(self, node):
    if node:
      print(node.data, end=' ')
      self.preorderrecursive(node.left)
      self.preorderrecursive(node.right)
  def postorder(self):
    self.postorderrecursive(self.root)
    print()
  def postorderrecursive(self, node):
    if node:
      self.postorderrecursive(node.left)
      self.postorderrecursive(node.right)
      print(node.data, end = ' ')
  def search(self, data):
    return self.searchrecursive(self.root, data)
  def searchrecursive(self, node, data):
    if node is None:
      return False
    if node.data == data:
      return True
    if data < node.data:
      return self.searchrecursive(node.left, data)
    else:
      return self.searchrecursive(node.right, data)
  def delete(self, data):
    self.root = self.deleterecursive(self.root, data)
  def deleterecursive(self, node, data):
    if node is None:
      return None
    #search for the node to delete
    if data < node.data:
      node.left = self.deleterecursive(node.left, data)
    elif data > node.data:
      node.right = self.deleterecursive(node.right, data)
    else:
      #case 1: leaf node(no children)
      if node.left is None and node.right is None:
        return None
      #case 2: one child
      elif node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      #case 3: two children
      else:
        successor = self.findmin(node.right)
        node.data = successor.data
        node.right = self.deleterecursive(node.right, successor.data)
    return node
  #findminimun node in a subtree
  def findmin(self, node):
    if node.left is None:
      return node
    return self.findmin(node.left)

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
bst.inorder()
bst.preorder()
bst.postorder()
print('search for 40', bst.search(40))
print('search for 100', bst.search(100))
bst.delete(20) # leaf node
bst.inorder() 
bst.delete(30)
bst.inorder()
bst.delete(70)
bst.inorder()
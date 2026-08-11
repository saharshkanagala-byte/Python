class BSTnode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.right = None
    self.left = None 
class DictionaryBST:
  def __init__(self):
    self.root = None
  def insert(self, key, value):
    self.root = self.insertrecursive(self.root, key, value)
  def insertrecursive(self,node,key,value):
    if node is None:
      return BSTnode(key, value)
    if key < node.key:
      node.left = self.insertrecursive(node.left, key, value)
    elif key > node.key:
      node.right = self.insertrecursive(node.right, key, value)
    else:
      node.value = value
    return node
  def search(self, key):
    return self.searchrecursive(self.root, key)
  def searchrecursive(self, node, key):
    if node is None:
      return None
    if node.key == key:
      return node.value
    if key < node.key:
      return self.searchrecursive(node.left, key)
    else:
      return self.searchrecursive(node.right, key)
  def display(self):
    return self.displayrecursive(self.root)
  def displayrecursive(self, node):
    if node:
      self.displayrecursive(node.left)
      print(node.key, ":", node.value)
      self.displayrecursive(node.right)


bst = DictionaryBST()
bst.insert('cat', ' A small domesticated carnovoirious animal')
bst.insert('apple', 'A fruit that grows on trees')
bst.insert('banana', 'A long curved fruit with a yellow skin')
bst.insert('zebra', 'An african wild horse with black and white stripes')
bst.insert('dog', 'A domesticated carnovoirious animal with a barking sound')
bst.insert('elephant', " A very large animal with ivory tusk")
bst.display()
print('definition of dog : ', bst.search('dog'))


    
    
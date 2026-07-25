'''
Instructions

Tarun and Vishal were working on a project. They were creating an online electronic store. They wanted to keep all types of products in different categories in the form of a tree. To help them, create a generic tree and add all the electronic items accordingly.

HINT:

class TreeNode: - Defines the TreeNode class.
def __init__(self, name): - Initializes a TreeNode instance with a given name and an empty list of children.
def add_child(self, child): - Appends a child node to the list of children.
def __repr__(self, level=0): - Returns a string representation of the tree starting from the current node. It includes the name of the current node and recursively calls __repr__ on its children, with increased indentation for each level.
Example usage:
Creates a root node "Electronics" and several child nodes representing categories like "Mobiles," "Laptops," etc.
Adds child nodes to their respective parent nodes to build a tree structure.
Prints the tree using print(root), which calls the __repr__ method to display the tree structure.
Overall, this code demonstrates how to create a tree structure using nodes and display the tree hierarchy using recursion and indentation.


'''

class TreeNode:
  def __init__(self, name):
    self.name = name
    self.children = []
  def add_child(self, child):
    self.children.append(child)
  def __repr__(self, level=0):
    ret = '\t'*level+self.name+'\n'
    for child in self.children:
      ret += child.__repr__(level + 1)
    return ret

root = TreeNode('Electronics')
mobiles = TreeNode('Mobiles')
laptops = TreeNode('Laptop')
tvaudio = TreeNode('Tv & Audio')
home = TreeNode('Home Appliances')
root.add_child(mobiles)
root.add_child(laptops)
root.add_child(tvaudio)
root.add_child(home)
smartphones = TreeNode('smartphone')
feature = TreeNode('feauture phone')
accsesories = TreeNode('accsesories')
mobiles.add_child(smartphones)
mobiles.add_child(feature)
mobiles.add_child(accsesories)
gaming = TreeNode('Gaming laptops')
Buisness = TreeNode('Buisness laptop')
lapacc = TreeNode('accsesories')
laptops.add_child(gaming)
laptops.add_child(Buisness)
laptops.add_child(lapacc)
tv = TreeNode('Television')
homethea = TreeNode('Home theaters')
headphones = TreeNode('Headphones')
tvaudio.add_child(tv)
tvaudio.add_child(homethea)
tvaudio.add_child(headphones)
fridge = TreeNode('Refrigerators')
wash = TreeNode('Washing machines')
micro = TreeNode('Microwaves')
home.add_child()
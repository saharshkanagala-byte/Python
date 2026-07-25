class RecipeNode:
  def __init__(self, name, isfolder=False):
    self.name = name
    self.isfolder = isfolder
    self.children = []
  def add_child(self, child):
    self.children.append(child)
  def remove_child(self, child_name):
    self.children = [child for child in self.children if child.name != child_name]

  def display(self, indent=0):
    print(' '*indent, ("+- " if self.isfolder is True else "- "), self.name)
    for child in self.children:
      child.display(indent + 1)

class RecipeManager:
  def __init__(self):
    self.root = RecipeNode("Recipes", isfolder = True)
  def add_recipe(self, name, isfolder = False):
    newrecipe = RecipeNode(name, isfolder)
    self.root.add_child(newrecipe)
  def delete_recipe(self,name):
    self.root.remove_child(name)
  def display_recipes(self):
    self.root.display()


manager = RecipeManager()
manager.add_recipe("Desserts", isfolder= True)
manager.add_recipe("Chocolate cake")
manager.add_recipe('Vanilla cupcakes')
manager.add_recipe('Dinner', isfolder= True)
manager.add_recipe('Spagetti Carbonara')
manager.add_recipe('Chicken stir fry')
manager.display_recipes()
print('Recipes after deleting "Chiken stir fry"')
manager.delete_recipe('Chicken stir fry')
manager.display_recipes()
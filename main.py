# class Node {
#   constructor(value){
#     this.left = null;
#     this.right = null;
#     this.value = value;
#   }
# }

# class BinarySearchTree {
#   constructor(){
#     this.root = null;
#   }
#   insert(value){
#     //Code here
#   }
#   lookup(value){
#     //Code here
#   }
#   // remove
# }

# const tree = new BinarySearchTree();
# tree.insert(9)
# tree.insert(4)
# tree.insert(6)
# tree.insert(20)
# tree.insert(170)
# tree.insert(15)
# tree.insert(1)
# JSON.stringify(traverse(tree.root))

# //     9
# //  4     20
# //1  6  15  170

# function traverse(node) {
#   const tree = { value: node.value };
#   tree.left = node.left === null ? null : traverse(node.left);
#   tree.right = node.right === null ? null : traverse(node.right);
#   return tree;
# }

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    newNode = Node(value)
    if self.root is None:
      self.root = newNode
      return
    currentNode = self.root
    while currentNode is not None:
      if newNode.value < currentNode.value:
        if currentNode.left is None:
          currentNode.left = newNode
          return
        else:
          currentNode = currentNode.left
      else:
        if currentNode.right is None:
          currentNode.right = newNode
          return
        else:
          currentNode = currentNode.right

  def lookup(self, value):
    branch = []
    currentNode = self.root
    while currentNode is not None:
      branch.append(currentNode.value)
      if value == currentNode.value:
        return [branch, currentNode.value, currentNode]
      elif value < currentNode.value:
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
    return None

  def remove(self, value):
    parentNode = None
    currentNode = self.root

    while currentNode.value != value:
      if value < currentNode.value:
        parentNode = currentNode
        currentNode = currentNode.left
      else:
        parentNode = currentNode
        currentNode = currentNode.right

    return [parentNode.value, currentNode.value]
        


myBST = BinarySearchTree()
myBST.insert(9)
myBST.insert(4)
myBST.insert(6)
myBST.insert(1)
myBST.insert(20)
myBST.insert(15)
myBST.insert(170)

print(myBST.lookup(1))
print(myBST.lookup(6))
print(myBST.lookup(15))
print(myBST.lookup(170))
print(myBST.remove(6))




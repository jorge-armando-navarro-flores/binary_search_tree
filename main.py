# 

# //     9
# //  4     20
# //1  6  15  170



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
    if self.root.value == value:
      return self.root.value
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
    if self.root is None:
      return False

    currentNode = self.root
    parentNode = None

    while currentNode is not None:
      if value < currentNode.value:
        parentNode = currentNode
        currentNode = currentNode.left
      elif value > currentNode.value:
        parentNode = currentNode
        currentNode = currentNode.right
      elif currentNode.value == value:
        #We have a match, get to work

        #option 1: no right child
        if currentNode.right is None:
          if parentNode is None:
            self.root = currentNode.left
          else:
            #if parent > current value, make current left child a child of parent
            if currentNode.value < parentNode.value:
              parentNode.left = currentNode.left
            elif currentNode.value > parentNode.value:
              parentNode.right = currentNode.left
        #option 2: Right child which doesn't have a left Child
        elif currentNode.right.left is None:
          currentNode.right.left = currentNode.left
          if parentNode is None:
            self.root = currentNode.right
          else:
            #if parrent > current, make right child of the left the parent
            if currentNode.value < parentNode.value:
              parentNode.left = currentNode.right
            elif currentNode.value > parentNode.value:
              parentNode.right = currentNode.right

        #option 3 right child that has a left child
        else:
          #find the right child's left most Child
          leftMost = currentNode.right.left
          leftMostParent = currentNode.right
          while leftMost.left is not None:
            leftMostParent = leftMost
            leftMost = leftMost.left
          
          #parent's left subtree is now leftmost's right subtree
          leftMostParent.left = leftMost.right
          leftMost.left = currentNode.left
          leftMost.right = currentNode.right

          if parentNode is None:
            self.root = leftMost
          else:
            if currentNode.value < parentNode.value:
              parentNode.left = leftMost
            elif currentNode.value > parentNode.value:
              parentNode.right = leftMost
        return True
    

    


myBST = BinarySearchTree()
myBST.insert(9)
myBST.insert(4)
myBST.insert(6)
myBST.insert(1)
myBST.insert(20)
myBST.insert(15)
myBST.insert(170)

myBST.remove(9)
print(myBST.lookup(1))
print(myBST.lookup(6))
print(myBST.lookup(15))
print(myBST.lookup(170))






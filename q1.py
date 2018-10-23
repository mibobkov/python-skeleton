# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

# import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  root = Node(0)
  for port in portfolios:
      root.insert(port)

  # root.PrintTree('')
  answer = getMaxValue(root, root)
  return answer

BITS = 16
class Node:
    def __init__(self, level):
        self.left = None
        self.right = None
        self.level = level

    def insert(self, data):
    # Compare the new value with the parent node
        if self.level == BITS:
            return
        if data & (2**(BITS-1-self.level)) > 0:
            if not self.right:
                self.right = Node(self.level+1)
            self.right.insert(data)
        else:
            if not self.left:
                self.left = Node(self.level+1)
            self.left.insert(data)

    def PrintTree(self, prefix):
        if self.level == BITS:
            print(prefix)
            return
        if self.left:
            self.left.PrintTree(prefix+'0')
        if self.right:
            self.right.PrintTree(prefix+'1')

def getMaxValue(node1, node2):
    if not node1 or not node2:
        return 0
    val = 0
    if (node1.left and node2.right) or (node1.right and node2.left):
        val += 2**(BITS-1-node1.level)
        max1 = getMaxValue(node1.right, node2.left)
        max2 = getMaxValue(node1.left, node2.right)
        val += max(max1, max2)
    else:
        max1 = getMaxValue(node1.right, node2.right)
        max2 = getMaxValue(node1.left, node2.left)
        val += max(max1, max2)
    return val


print('Answer: ' + str(question01([31, 9, 7, 12])))
# print('Answer: ' + str(question01([1, 9])))
# print('Answer: ' + str(question01([2**15, 4])))
# print('Answer: ' + str(question01([2**16-1, 9,1,4,2,1,6,467,657,45,674,567,456,745,674,5672,354,345,54366,34562,23455,23451,53425, 7, 12])))



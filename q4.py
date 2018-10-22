# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  accTime = 0
  bestTime = -1
  list = LinkedList()
  for row in rows:
    for machine in row:
      if machine == 'X':
        if list.size == numberMachines:
            if bestTime == -1:
                bestTime = accTime
            elif accTime < bestTime:
                bestTime = accTime
        accTime = 0
        list = LinkedList()
      else:
        time = int(machine)
        if list.size < numberMachines:
            list.insert(time)
            accTime += time
        else:
            accTime -= list.first
            accTime += time
            list.delete()
            list.insert(time)
    if list.size == numberMachines:
        if bestTime == -1:
            bestTime = accTime
        elif accTime < bestTime:
            bestTime = accTime
    accTime = 0
    list = LinkedList()
  # modify and then return the variable below
  if bestTime == -1:
      return 0
  return bestTime

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insert(self, x):
        self.size += 1
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def delete(self):
        self.size -= 1
        self.first = self.first.next

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

# print(question04([['X', 'X', 2], [2, 3, 'X'], ['X', 3, 2]], 3))

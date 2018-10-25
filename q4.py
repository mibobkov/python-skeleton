# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  accTime = 0
  bestTime = -1
  size = 0
  for row in rows:
    for i in range(len(row)):
      machine = row[i]
      if machine == 'X':
        if size == numberMachines:
            if bestTime == -1 or accTime < bestTime:
                bestTime = accTime
        accTime = 0
        size = 0
      else:
        time = int(machine)
        if size < numberMachines:
            accTime += time
            size += 1
        else:
            if bestTime == -1 or accTime < bestTime:
                bestTime = accTime
            accTime -= row[i-size]
            accTime += time
    if size == numberMachines:
        if bestTime == -1 or accTime < bestTime:
            bestTime = accTime
    accTime = 0
    size = 0

  # modify and then return the variable below
  if bestTime == -1:
      return 0
  return bestTime

#print(question04([['X', 2, 2], [2, 3, 'X'], ['X', 3, 2]], 2))

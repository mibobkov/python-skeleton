# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

# import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  map = times[0][:]
  for i in range(numServers):
    for j in range(numServers):
        if j == i:
          continue
        if map[i] + times[i][j] < map[j]:
          map[j] = map[i] + times[i][j]
  return map[targetServer]

print(question06(3,1,[[0,7,4],[7,0,2],[4,2,0]]))

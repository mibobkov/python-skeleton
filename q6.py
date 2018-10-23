# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

# import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below

  sofar = times[0][:]
  reached = [0]
  for iter in range(numServers-1):
      # print('Reached: ' + str(reached))
      for r in reached:
          for i in range(numServers):
              if i == r:
                  continue
              if times[r][i] + sofar[r] < sofar[i]:
                  sofar[i] = times[r][i] + sofar[r]
      minVal = -1
      for s in range(len(sofar)):
          if s in reached:
              continue
          elif minVal == -1 or minVal > sofar[s]:
              minVal = sofar[s]
              minInd = s
      reached.append(minInd)
      if targetServer in reached:
          return sofar[targetServer]
  return sofar[targetServer]

# print(question06(3,1,[[0,7,4],[7,0,2],[4,2,0]]))

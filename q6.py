# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

# import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  sofar = times[0][:]
  for i in range(numServers):
      times[i][0] = 9223372036854775807
  reached = set([0])
  reachedMins = {}
  reachedMinsInds = {}
  recalc = reached
  for iter in range(numServers-1):
      # print('Reached: ' + str(reached))
      minMinValue = 9223372036854775807
      for r in recalc:
          minValue = min(times[r])
          minInd = times[r].index(minValue)
          reachedMins[r] = minValue
          reachedMinsInds[r] = minInd
      for r in reached:
          minValue = reachedMins[r]
          if minValue < minMinValue:
              minMinValue = minValue
              minMinInd = reachedMinsInds[r]
              minMinOwner = r
      recalc = set([minMinOwner])
      recalc.add(minMinInd)
      sofar[minMinInd] = minMinValue
      reached.add(minMinInd)
      for i in range(numServers):
          times[i][minMinInd] = 9223372036854775807
      for i in range(numServers):
          times[minMinInd][i] += sofar[minMinInd]
      if targetServer in reached:
          return sofar[targetServer]
  return sofar[targetServer]

# import time
# import random
# SIZE = 500
# random.seed(42)
# times = []
# for i in range(SIZE):
#     row = []
#     for j in range(SIZE):
#         if i == j:
#             row.append(0)
#         else:
#             row.append(random.randint(1, 100))
#     times.append(row)
# start = time.time()
# print(question06(SIZE,1,times))
# end = time.time()
# print(end-start)
# #0.054

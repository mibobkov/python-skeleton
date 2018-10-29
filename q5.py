# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

# import numpy as np

def question05(allowedAllocations, totalValue):
  return q5alter(allowedAllocations, totalValue)
#   nums = []
#   for i in range(0, totalValue+1):
#       nums.append(-1)
#   for n in allowedAllocations:
#       nums[n] = 1
#   for i in range(0, totalValue+1):
#       if nums[i] == -1:
#           continue
#       for allocation in allowedAllocations:
#           nextNum = i + allocation
#           if nextNum <= totalValue and (nums[nextNum] == -1 or nums[nextNum] > nums[i] + 1):
#               nums[nextNum] = nums[i]+1
#   return nums[totalValue]

def q5alter(allowedAllocations, totalValue):
  allowedAllocations = sorted(allowedAllocations)
  allowedAllocations.reverse()
  return q5helper(allowedAllocations, 0, 0, totalValue)
  
  # modify and then return the variable below

def q5helper(allowedAllocations, allocated, already, target):
  if already > target:
    return -1
  if already == target:
    return allocated
  minVal = 123124152352345
  for al in allowedAllocations:
    res = q5helper(allowedAllocations, allocated+1, already+al, target)
    if res != -1:
      if res < minVal:
        minVal = res
  return minVal

# import time
# start = time.time()
# print(question05([1, 3, 4], 12))
# end = time.time()
# print(end-start)
# start = time.time()
# print(q5alter([3, 4], 13))
# end = time.time()
# print(end-start)

# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
  nums = []
  for i in range(0, totalValue+1):
      nums.append(-1)
  for n in allowedAllocations:
      nums[n] = 1
  for i in range(0, totalValue+1):
      for allocation in allowedAllocations:
          prevNum = i - allocation
          if prevNum > 0 and nums[prevNum] > 0:
              if nums[i] == -1 or nums[i] > nums[prevNum] + 1:
                  nums[i] = nums[prevNum] + 1
  return nums[totalValue]

  # modify and then return the variable below


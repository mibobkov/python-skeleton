# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
  nums = []
  for i in range(0, totalValue+1):
      nums.append(-1)
  for n in allowedAllocations:
      nums[n] = 1
  for i in range(0, totalValue+1):
      if nums[i] == -1:
          continue
      for allocation in allowedAllocations:
          nextNum = i + allocation
          if nextNum <= totalValue and (nums[nextNum] == -1 or nums[nextNum] > nums[i] + 1):
              nums[nextNum] = nums[i]+1
  print(nums)
  return nums[totalValue]

  # modify and then return the variable below


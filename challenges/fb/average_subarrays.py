# Find subarrays whose avg sum is GREATER THAN the avg sum of remaining elements in array.
# return start, end of each subarray
# This problem came in the mock interview for Facebook Interview Prep.


def aboveAverageSubarrays(A):
  print("In:", A)
  # use presum
  # compute the average of a subarray L1,R1 with (presum[R1] - presum[L1]) / (R1-L1)
  N = len(A)
  presum = [0 for _ in range(N+1)]
  A = [-1] + [x for x in A]  # 1-based indexes
  
  for i in range(1, N+1):
    presum[i] = A[i] + presum[i-1]
  
  print("presum:")
  print(presum)
  print("A")
  print(A)
  
  subarrays = []
  
  # For every possible start and end
  # we don't need to check empty arrays
  for st in range(1, N+1):
    for ed in range(st, N+1):  # ed is inclusive
      #print("Sub:", st,ed)
      # subarray
      N_in = ed - st + 1
      # the rest
      N_out = st-1 + N-ed

      restLeft = presum[st-1] # sum to the left
      restRight = presum[N] - presum[ed] # sum to the right
      
      avgIn = (presum[ed] - restLeft) / N_in
      #print("-avg in", avgIn)
      avgOut = (restLeft + restRight) / (N_out) if N_out>0 else 0
      #print("-avg out", avgOut)
      
      if avgIn > avgOut:
        #print("...append", st, ed)
        subarrays.append([st, ed])
        
  return subarrays

## TESTING
  
# print("RESULT", aboveAverageSubarrays([1000,900,2,50,50]))
# print()
# print("RESULT", aboveAverageSubarrays([3,4,2]))
# print()
# print("RESULT", aboveAverageSubarrays([3,-20, 4]))
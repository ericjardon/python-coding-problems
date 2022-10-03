import sys

def solution(A):
  """Your solution goes here."""
  def minDifference(sumA, sumB, i, arr, bestDiff):
    # Either give to server A or B
    if i == len(arr):
      return abs(sumA - sumB)
    # find best of either option
    giveA = minDifference(sumA + arr[i], sumB, i+1, arr, bestDiff)
    giveB = minDifference(sumA, sumB + arr[i], i+1, arr, bestDiff)
    return min(giveA, giveB)
    
  if len(A) == 1:
    return A[0]
  
  return minDifference(0, 0, 0, A, 100001)
    
  


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()

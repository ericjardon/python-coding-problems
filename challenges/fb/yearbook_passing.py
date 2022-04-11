import math
from copy import copy
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findSignatureCounts(arr):
  # Arr is a permutation of 1..n. No repetitions
  
  # every minute, every student i signs the current yearbook, and passes
  # it to student in arr[i-1].
  # when a student receives their yearbook they stop passing it around.
  
  # input guarantees every student eventually receives their own book.
  
  # compute a list where every element i-1 is equal to the number of signatures in a student's yearbook.
  N = len(arr)
  in_circulation = {i+1 for i in range(N)}  # yearbooks ids still in circulation
  book_where = [i for i in range(N+1)]      # book at index i is at a[i]
  output = [0 for _ in range(N)]
  
  while len(in_circulation):
    # Add a signature at ouptut[i-1] for every element in circulation. Check if it arrived to owner.
    
    for book in copy(in_circulation):
      output[book-1] += 1  # increment signatures
      
      # update holder
      i = book_where[book]
      book_where[book] = arr[i-1]
      
      # remove book from circulation if it arrives to owner
      if book_where[book] == book:
        in_circulation.remove(book)
  
  
  return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1]
  expected_1 = [2, 2]
  output_1 = findSignatureCounts(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2]
  expected_2 = [1, 1]
  output_2 = findSignatureCounts(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  
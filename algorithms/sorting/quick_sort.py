

from multiprocessing.sharedctypes import Value
from tkinter import N


def swap(arr, i, j):
    if 0<=i<len(arr) and 0<=j<len(arr): 
        arr[i], arr[j] = arr[j], arr[i]
    else:
        raise ValueError(f'Indexes {i} {j} in array of lenght {len(arr)}')


def quickSortStart(A: list) -> None:
    # Modifies in place, single swap flavor, pivot is start
    def partition(A: list, st: int, ed: int) -> int:
        pivot_index = st
        pivot = A[pivot_index]

        # Until start and end cross each other
        while st < ed:
            # Increment st until element larger than pivot
            while st < len(A) and A[st] <= pivot:
                st += 1

            # Decrement ed until element less than pivot
            while A[ed] > pivot:
                ed -= 1
            
            # Swap the first element larger than pivot with the 
            # last element smaller than pivot
            if (st < ed):
                print("Swap", A[st], A[ed])
                swap(A, st, ed)
            
            # Put pivot in its right place
        print("swapping pivot", A[pivot_index], "with", A[ed])
        swap(A, ed, pivot_index)
            
        return ed

    def quick(A, st, ed) -> None:
        if st < ed:
            pivot = partition(A, st, ed)
            print(A)
            # Sort elements before and after partition
            quick(A, st, pivot-1)
            quick(A, pivot+1, ed)
    
    quick(A, 0, len(A) - 1)


def quickSortLast(A: list) -> None:
    '''takes last elem as pivot, places pivot in correct position,
        places all smaller elemes to the left; all greater elems to the right'''
    def partition(A, lo, hi):
        pivot = A[hi]               # last elem in A[lo:hi+1]

        i = lo - 1                  # i will hold index of last element smaller than pivot

        for j in range(lo, hi):     # traverse up to pivot, exclusive
            if A[j] < pivot:        # smaller elements are placed to the beginning of array
                i += 1
                swap(A, i, j)

        # after the loop, A[i] is the last element smaller than pivot.
        swap(A, i+1, hi)            # Place pivot A[hi] in its 'correct' position: i+1
        return i + 1
    
    def quickSort(A, lo, hi):
        if lo < hi:  # prevents index out of bounds
            print("Pivot", A[hi], end=' ')
            pivot_index = partition(A, lo, hi)
            print(A)
            # Separately sort subarrays of smaller elems than pivot and larger elems than pivot
            quickSort(A, lo, pivot_index-1)
            quickSort(A, pivot_index+1, hi)

    n = len(A)
    quickSort(A, 0, n-1)

arr = [3, 18, 2, 5, 4, 1, 21, 4, 12,2 ,5,342 ,123 ,1, 3.3,7, 7,3 ,7 ,2,5, 43, 2,4, 6]
print("Init", arr)
quickSortLast(arr)
print(arr)
'''
A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
'''
import bisect # for inserting in a sorted array. Every insertion is O(N) unless we use a home-cooked linked list
class MyCalendarThree:

    def __init__(self):
        self.lefts = []
        self.rights = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.lefts, start)
        bisect.insort(self.rights, end)
        # Loop through the left side and keep track of how many you have 
        left_total = 0
        right_total = 0
        curr_max = 1  # At least one booking will be made
        
        while left_total < len(self.lefts) - 1:
            left_total += 1
            while self.lefts[left_total] >= self.rights[right_total]:
                right_total += 1
            curr_max = max(curr_max, left_total - right_total + 1)
            
        return curr_max


## TEST CASES

# book calls:
# [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]
# expected outputs:
# 1, 1, 2, 3, 3, 3
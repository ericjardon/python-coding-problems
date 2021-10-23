"""In an infinite straight segment of race, cars cannot overtake one another.
    And their speed can't be higher than the car in front: at most it is equal.
    Given a list of the max speed of N cars in the order they entered
    the segment, count how many cars are moving at their max speed.
    + Assume all speeds are unique, int
    """

#There is at least one car moving at max speed, namely the first.
# we can assume they are all at max and substract 1 by one when we find an element that is larger than the one preceding it.
# Use a list of real speeds to know at what speed each car is going. A trailing car can have a speed equal or less than the one
# in front of it.
# Go through the list filling up a real speeds list, filling each entry based on the preceding cars speed.
# Compare values at max and real in the same index to count.

def carsAtMax(speeds):
    speeds = [int(i) for i in speeds]
    cars = len(speeds)
    for i in range(1,len(speeds)):
        if speeds[i] > speeds[i-1]:
            # if the car's max speed is larger than the speed of the one before it
            cars -= 1   # there is one less car who is at max speed
            speeds[i] = speeds[i-1] # the car lowers to match the speed of the car in front
    return cars

try:
    T = int(input())
    for _ in range(T):
        cars = int(input())
        s = input()
        if cars>0:
            speeds = s.split(" ")
            print(carsAtMax(speeds))
        else:
            print(0)
except:
    pass
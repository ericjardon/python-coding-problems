# 2 person code breaking game
# 1 person creates a sequence
# n colored pegs (duplicated allowed)
# this sequence is the code

# other player must determine the code by making guesses
# every guess consists of n colored pegs

# After a guess, we get feedback of how close we are
# feedback is a tuple r,s, where r= # pegs identical in color and position
# s = number of remaining pegs identical in color but not in position

'''
NOTE: this is equivalent to wordle checker machine
with n-sized words.

Once pegs in the original code have been "matched",
they cannot be matched with any other pegs.

Determine feedback r and s given a code and a guess.
'''

from collections import Counter
N, code, guess = input().split()  # < 50
N = int(N)

# Both made of uppercase, alphabetic
pegs = Counter(code)
pos_matched = set()

# r = pegs identical in color and position (green)
# s = remaining pegs identical in color but not position (yellow)
r = 0
s = 0
for i in range(N):
    if guess[i] == code[i] and pegs[code[i]] > 0:
        r += 1
        pos_matched.add(i)
        # update counter
        pegs[guess[i]] = pegs[guess[i]] - 1

# from pprint import pprint
# pprint(pegs)

for i in range(N):
    if i in pos_matched:
        continue
    if guess[i] in pegs and pegs[guess[i]] > 0:
        # Check if there are remaining to be matched
        s += 1
        # update counter
        pegs[guess[i]] = pegs[guess[i]] - 1

print(r, s)

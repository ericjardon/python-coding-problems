# IMPLEMENTATION NOT MY OWN
'''
Given two words `begin` and `end`, and a dictionary of words with same length L,
find the least number of transformations from begin to end, changing one character
at a time and using the words in the dictionary. 
Return 0 if no such transformation exists.
'''
from collections import deque


def wordLadderLength(begin: str, end: str, word_list: list[str]) -> int:
    q = deque()
    q.append(begin)
    visited = set()
    visited.add(begin)

    word_list = set(word_list)
    charset = 'abcdefghijklmnopqrstuvwxyz'
    depth = 1  # depth of the state tree = number of transformations

    # Breadth First Search
    while q:
        size = len(q)
        # For every word enqueued in the previous transformation (same-level states)
        for _ in range(size):
            current_state = q.popleft()

            if current_state == end:
                return depth

            # For every position in current word
            for i in range(len(current_state)):
                # For every possible character
                for c in charset:
                    word = current_state[:i] + c + current_state[i+1:]

                    # If word is valid and has not been used before
                    if word in word_list and word not in visited:
                        q.append(word)
                        visited.add(word)

        # Next level in the state tree
        depth += 1

    # end word is never found, return 0
    return 0

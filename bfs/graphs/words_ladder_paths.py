'''
An extension over the Word Ladder problem:
Given two words `begin`, `end` and a set of words,
return all the shortest paths from begin to end, one
transformation (single-character change) at a time using 
only valid words from the wordset.
'''
from collections import deque
from collections import defaultdict  # to provide a default for missing keys
from pprint import pprint  # to pretty print a dictionary


def findWordLadders(begin: str, end: str, wordlist: list[str]) -> list[list[str]]:

    def get_intermediates(word: str):
        """
        Returns a set containing all versions of the given word
        with wildcard character * at every position
        """
        return {word[:i] + '*' + word[i+1:] for i in range(len(word))}

    ans = []  # list of shortest paths

    if end not in wordlist:    # edge case
        return ans

    # nodes (string keys) mapped to a set of their neighbors
    graph = defaultdict(set)

    # Populate the graph
    for word in wordlist:
        # Generate intermediate strings of every word
        # e.g. hot -> {*ot, h*t, ho*}
        adjacencies = get_intermediates(word)

        graph[word] = adjacencies

        # Add the word to every adjacency's adjacency set
        for adj in adjacencies:
            graph[adj].add(word)

    # reference value to select valid paths, updated when we first encounter end word
    min_cost = None
    visited = set()  # to discard already-seen nodes and avoid entering traversal loops

    # Enqueue triplets: (current_word, current_cost, current_path)
    start = (begin, 1, [begin])
    q = deque([start])

    # Breadth-first Search, saving accumulated paths to a list. until we reach end word we can append to answer
    while q:

        curr_word, curr_cost, curr_path = q.popleft()
        # For every adjacency of the popped word
        for adj in graph[curr_word]:
            # If end word is reached and path cost is minimum
            if adj == end and (min_cost is None or min_cost == curr_cost+1):
                # update value for min cost, only changes when end is first encountered
                min_cost = curr_cost + 1
                # complete our current path with end word
                curr_path.extend([end])

                # add this path to our list of answers
                ans.extend(curr_path)

            if adj not in visited:             # If neighbor has not been explored

                if adj in wordlist:  # adj is a literal word, e.g. "bed"
                    # enqueue next state, extending the current path
                    q.append((adj, curr_cost, curr_path + [adj]))

                else:       # adj is an intermediate string, "b*d"
                    # enqueue next state, adding one transformation to path cost.
                    # Path cost is given by the num of intermediate strings from begin to end.
                    q.append((adj, curr_cost + 1, curr_path))

        # Mark current word as visited after checking all its neighbors
        visited.add(curr_word)

    # After while loop ends, we have traversed all possible non-repeating paths to end word
    # we only stored in ans the paths with minimum cost
    return ans


if __name__ == "__main__":
    wordset = ["ted", "tad", "bed", "bad", "bot", "bet",
               "bat", "bar", "tar", "car", "cam", "com", "bom", "bod"]

    begin = "ted"
    end = "com"

    paths = findWordLadders(begin, end, wordset)
    print(paths)



## Variant: single-best path. The first path encountered is necessarily the best
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:        
        # Create graphs for transitioning
        wordList = set(wordList)
        if endWord not in wordList: return []
        wordList.add(beginWord)
        
        graph = {}
        
        for w in wordList:
            neighbors = set([w[:i] + '*' + w[i+1:] for i in range(len(w))])
            graph[w] = neighbors
            
            for n in neighbors:
                if n in graph:
                    graph[n].add(w)
                else:
                    graph[n] = set([w])
        
        # print('graph')
        # from pprint import pprint
        # pprint(graph)
        
#         # Perform BFS for shortest path
        from collections import deque
        
        path = []
        visited = set()
        q = deque()
        q.append((beginWord, [beginWord]))
        
        while q:
            w, currPath = q.popleft()
            if w == endWord:
                # Finish
                return currPath

            # explore neighbors if unvisited
            for neighbor in graph[w]:
                if neighbor not in visited:
                    if neighbor in wordList:
                        q.append((neighbor, currPath + [neighbor]))
                    else:
                        q.append((neighbor, currPath))
            
            visited.add(w) 
    
        return []
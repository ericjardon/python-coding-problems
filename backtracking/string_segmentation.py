'''
Given a set of words and a large string, determine if it can be completely
segmented into words contained in the set, e.g. 'applepenapple' 
given a set {apple,pen} should return True
----
We can use a Trie structure to solve this problem as it simplifies the parsing
of words in a string.
'''


class TrieNode:
    def __init__(self) -> None:
        self.children = {}   # chars as keys
        self.isWord = False  # set to True on insertions


class StringSegmentation:
    """
    Uses backtracking to traverse every index of longstring, attempting to segment if a word
    is reached in Trie.
    Can only traverse trie if the characters match a path in Trie.
    """
    def insertToTrie(self, root: TrieNode, word: str) -> None:
        current_node = root
        for char in word:
            # Traverse down the tree
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        # Last char of the word, mark as valid word
        current_node.isWord = True

    def buildTrie(self, words: set) -> TrieNode:
        root = TrieNode()       # empty string ""
        for w in words:
            self.insertToTrie(root, w)
        return root

    def isSegmentable(self, longstring: str, words: set) -> bool:
        """
        Driver that implements recursion to determine if a given string can be completely
        segmented into valid words from a set of strings
        """
        # Edge case: no words or longstring
        if len(words) == 0 or len(longstring) == 0:
            return False

        trie = self.buildTrie(words)

        def segmentRec(string: str) -> bool:
            # If empty string, we finished segmenting
            if string == "":
                return True

            curr_node = trie   # start at root of trie
            ans = False     # default to False, set True when solution found
            
            # traverse string, restart at root node when a word is found
            for i in range(len(string)):
                ch = string[i]
                # If character in trie, continue traversal
                if ch in curr_node.children:
                    curr_node = curr_node.children[ch]
                    if curr_node.isWord:
                        # segment found, recurse on remaining string from here
                        if segmentRec(string[i+1:]):
                            ans = True
                            break
                else:
                    # not segmentable from here
                    break
            return ans
        # Use the trie of given words to check at every index of longstring if 
        # it is a valid path down Trie. 
        # When we reach an endword node, recurse: next index from the top of the trie
        return segmentRec(longstring)


if __name__ == "__main__":

    wordsets = [
        {"done", "bar", "zone"},
        {"apple", "app", "and", "pen", "lepen"},
        {"sam", "puts", "foo", "bit"},
        {"Hello", "I", "am", "Eric"},
        {"Hello", "I", "am", "Eric"}
    ]

    strings = [
        "zonebardonebar",
        "applepen",
        "samputsf",
        "HelloEricEricEric",
        "HelloEri"
    ]

    answers = [True, True, False, True, False]
    testcases = len(answers)
    solver = StringSegmentation()

    for i in range(testcases):
        long = strings[i]
        wset = wordsets[i]

        if solver.isSegmentable(long, wset) == answers[i]:
            print(f"Test {i} passed")
        else:
            print(f"Test {i} failed: expected {answers[i]}")

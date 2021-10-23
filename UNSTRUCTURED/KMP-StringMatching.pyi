# KMP is an optimized algorithm for matching a short string in a very large text.
# We want to know whether the string occurs once in the text.
# Let 'patt' be the string to match of size m, 'text' the text to search of size n

## Naive Method
def naiveSM(patt: str, text: str):
    # in python, strings do not end with the null character '\0' but we can traverse the string with simple for loops
    for i in range(len(text)):  # for every possible position in text
        j=0
        while (i+j<len(text) and j < len(patt) and patt[j] == text[i+j]): j += 1
        if j == len(patt):  # found a match
            return True
        i += 1
    return False
    # Time complexity O(n*m) worst case

## Skipping iterations of outer loop (through text) based on previously seen characters
# example: text "banananananonanano", patt "nano",
# the algorithm may be tempted to check through all 'nan's making it very slow.
# however we can optimize: after having a partial match of say, 3 characters, in the next pos
# we know what is in the next (3-1) positions of the text.

def skippingSM(patt: str, text: str):
    def overlap(x: str, y: str):        # NOT VERIFIED. Real overlap function may be something else
        # longest word that is suffix of x AND prefix of y
        i=1
        overlap = 0
        while (i < len(x)):       # start from x's second position and shift y 1 position forward as long as they are diff
            if x[i] != y[0]:
                i+=1
                continue
            j = 0
            while (i+j < len(x) and j < len(y) and x[i+j] == y[j]): i+=1;
            overlap = max(overlap, j) # j is the max number of chars matched in this iteration
            i+=1
        return overlap

    n = len(text)
    i=0
    while(i<n):
        j=0
        while (i+j < n and j < len(patt) and text[i+j]==patt[j]): j+=1
        if j == len(patt): return True   # found match
        # else, skip by moving i to the next
        i = i + max(1, j - overlap(patt[:j], patt))

# Skipping inner iterations involves avoiding checking characters that were already matched in the overlap with previous match.
# https://www.ics.uci.edu/~eppstein/161/960227.html
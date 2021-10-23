# GOGLE CHALLENGE 1
"""Given a Set of words D and a string S, find the longest word
    in D that is a subsequence (non-contiguous) contained in S.
    A subsequence W is a sequence of characters (len >=0) that can
    be taken from S without replacement and in sequential order."""
import math
# for complexity analysis only

S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}
S1 = "chgrughahahaaspolinesiadjsvoewnfiuawvbdsñkcjsaklÑNCericISAOÑcbejwndsjalncrueiahfuiobcsajHJLfeungueiaofndihoscNJASkflnsdjkcjklBCJKSLABcjkslahBSDJAKLCJDSHVJKDFLNVLHUSAIILhjdkslhljvhuisahvuidshvndsaihviodsnavi" \
     "crueiahfuiobcsajHJLfeungueiaofndihoscNJASkflnsdjkcjklBCJKSLABcjkslahBSDJAKLCJDSHVJKDFLNVLHUSAIILhjdkslhljvhuisahvuidshvndsaihviodsnavi" \
     "crueiahfuiobcsajHJLfeungueiaofndihoscNJASkflnsdjkcjklBCJKSLABcjkslahBSDJAKLCJDSHVJKDFLNVLHUSAIILhjdkslhljvhuisahvuidshvndsaihviodsnavi"
D1 = {"polineasjchgrughahahaassiadjsvoewnfiuadh""ch", "grug", "hahaha", "as", "polinesiaerici", "A", "dcsjk", "jd", "djc", "yer", "sjfkjl", "ancsj"
      "aaaaaaaa", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"}

# GREEDY APPROACH.
def findLongest(S, D):
    # Sort the words by length in descending order, so our first find is the answer.
    #ops = 0
    words = sorted(list(D), key=len, reverse=True)      # Convert the set to a list so we can sort it
    #ops += len(words) * math.ceil(math.log(len(words)))
    answer = ""
    # For each word, check character-by-character for a match.
    for w in words:
        #ops += 1
        if len(w) > len(S):
            # skip to next word if word is larger than S
            continue
        i = 0   # index for traversing w
        j = 0   # index for traversing S
        count = len(w)
        while (j<len(S) and count>0):
            # Stop when finished traversing S
            #ops += 1
            if w[i] == S[j]:
                # If it matches, reduce the count and move both indexes.
                count -= 1
                i += 1
                j += 1
            else:
                # If it doesn't, move to next character in S.
                j += 1
        #ops += 1
        if count == 0:
            # if all characters of word were found, it is the longest match
            # and we have our answer
            answer = w
            break
    #print("ops 1:",ops)
    return answer

# IMPROVED GREEDY USING INDEX MAPPING
# Preprocess S so we have a mapping of characters to indices
# When we want to match a character of w, if our last index matched was X, we need to find the smallest index Y for
# such character. At any point, if no index larger than x is found, then w is not a subsequence.
# Use binary search to look for the index.

def preprocess(S):
    map = {}
    for i in range(len(S)):
        c = S[i]
        if c in map:
            map[c].append(i)
        else:
            map[c] = [i]
    return map

def bSearch(X, indices):
    # X is the index of previously matched character in S
    # indices is the sorted list of positions for a character
    # Finds the smallest number in list larger than X
    lo = 0
    hi = len(indices) - 1
    ans = -1
    while lo<=hi:
        # Guarantees search space is 2 or more elems
        i = (lo + hi) // 2      # floor division for both int and float args
        if indices[i] < X:
            lo = i+1
        elif indices[i] > X:
            ans = indices[i]
            hi = i-1
        else:
            # return the next position in the list
            if (i+1) < len(indices):
                ans = indices[i + 1]
            break
    return ans

def findLongest2(S, D):
    #ops = 0
    map = preprocess(S)
    #ops += len(S)
    maxlen = 0
    ans = ""
    for word in D:
        #ops += 1
        if len(word) > maxlen:
            X = -1
            found = True
            for char in word:
                #ops += 1
                if char in map:
                    #ops += math.ceil(math.log(len(map[char])))
                    Y = bSearch(X, map[char])
                    #ops += 1
                    if Y == -1:
                        # next index was not found
                        # i.e. word is not a subsequence so we skip
                        found = False
                        break
                    X = Y
            #ops += 1
            if found:
                ans = word
                maxlen = len(word)
    #print("ops 2:",ops)
    return ans

print("eric approach ",findLongest(S1, D1))
print("google approach ", findLongest2(S1,D1))

# Result: success
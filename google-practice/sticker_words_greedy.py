"""
We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.
"""
# INCORRECT SOLUTION

from collections import defaultdict
from typing import List

class SolutionGreedy:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # choose the sticker with the least distance to target.
        # aka the sticker that has most letters we can use.
        # first approach: use maps
        print("PARAMS:", stickers, ",", target)
        
        def getCharCount(string):
            # Returns dict of character count
            c_count = {}
            for c in string:
                if c in c_count:
                    c_count[c] += 1 
                else:
                    c_count[c] = 1
            return c_count
        
        def getScore(t, w):
            # Returns the number of letters in stckr that target can use
            score = 0
            for c in t:
                if c in w:
                    score += min(t[c], w[c])
            return score
        
        def addToLetterPool(pool, sticker_count):
            # Adds stickers' char count to pool
            for c in sticker_count:
                pool[c] += sticker_count[c]
            return pool
                
        def findBestSticker(letters, t_count):
            # Iterates over words, returns the key of the most useful one
            # If no word helps, return None
            best = None
            bestScore = -1
            for word in letters:
                score =  getScore(t_count, letters[word])
                if score > bestScore:
                    bestScore = score
                    best = word

            # No sticker helps
            if bestScore == 0: 
                return None

            return best
        

        # Get count vectors of stickers
        letters = {}
        for sticker_word in stickers:
            count = getCharCount(sticker_word)
            letters[sticker_word] = count
        
        # Get count vector of target
        target_count = getCharCount(target)
        
        # Init letter pool
        pool = defaultdict(int) # 0 if char not present
        
        n_letters = len(target)
        
        answer = 0
        
        missing = {} # remember letters we did not have so we don't loop
        needSticker = True

        while n_letters > 0:
            # pick sticker if needed
            if needSticker:
                sticker_to_use = findBestSticker(letters, target_count)
                if sticker_to_use is None: 
                    print("no useful sticker")
                    return -1
            
            answer += 1 # number of stickers used

            # add sticker to pool
            print("adding", sticker_to_use, "to pool")
            pool = addToLetterPool(pool, letters[sticker_to_use])

            # Substract letters from target using pool, full pass
            needSticker = False
            for c, count in list(target_count.items()):
                if count==0:
                    print("remove from target:", c)
                    target_count.pop(c)
                else: # use c from pool
                    if pool[c] == 0:
                        print(c, "missing, get new sticker")
                        # need new sticker
                        needSticker = True
                    else:
                        missing.pop(c, None)
                        print(c, "in pool times:", pool[c])
                        letters_taken = min(pool[c], target_count[c])
                        target_count[c] -= letters_taken    # substract from target
                        pool[c] -= letters_taken            # substract from letter pool
                        n_letters -= letters_taken          # substract from total tally
                        print("n_letters remain:", n_letters)
        print("sticker used", answer)
        return answer
        
    
# stickers = ["with","example","science"]; target = "thehat"
# if Solution().minStickers(stickers, target) == 3: 
#     print("OK") 
# else: 
#     print("INCORRECT")

# stickers = ["notice","possible"]; target = "basicbasic"
# if Solution().minStickers(stickers, target) == -1: 
#     print("OK") 
# else: print("INCORRECT")
            
stickers = ["these","guess","about","garden","him"]
target = "atomher"
if Solution().minStickers(stickers, target) == 3: 
    print("OK") 
else: print("INCORRECT")
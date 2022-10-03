from copy import deepcopy
from typing import List
# https://leetcode.com/problems/stickers-to-spell-word/discuss/2425982/Go.-Backtracking.-Faster-100

# def getCharCount(string):
#     # Returns dict of character count
#     c_count = {}
#     for c in string:
#         if c in c_count:
#             c_count[c] += 1 
#         else:
#             c_count[c] = 1
#     return c_count

# class Solution:

#     def minStickers(self, stickers: List[str], target: str) -> int:
#         # map letters of target to possible uses.
#         # maybe use brute force with back tracking?
#         t = getCharCount(target)
#         # Map every character to possible words
#         sticker_map = {}
#         for s in stickers:
#             sticker_map[s] = getCharCount(s)
    
#         have_letter = {}
#         for char in t:
#             have_letter[char] = [s for s, count in sticker_map.items() if char in count]
#         return self.stickersNeeded(target, 0, t, have_letter, sticker_map, 1000)
    
#     def canFormWord(string, i, char_count, have_letter, sticker_map, n_stickers):
#         candidates = sticker_map[string[0]]
#         if not candidates:
#             return -1
        
#         best = 1000
#         for c in candidates:
#             t = deepcopy(char_count)
#             for 
#             used = self.stickersNeeded()


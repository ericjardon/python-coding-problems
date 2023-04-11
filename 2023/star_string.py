from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        # It is more efficient to build a new string
        # than to modify the existing one.

        # We could build a set of indexes of characters to keep.
        # by identifying the non-star characters to delete.

        # 1. Reading RTL. Collect pairs of (rightmost star, leftmost nonstar) indexes, slices to delete.
        # 2. For a given slice, the leftmost nonstar is computed by counting number of consecutive stars,
        # adding this offset (num of nonstars to delete) to the leftmost consecutive star index.
        # 3. If this offset is larger than the number of characters between one star and another,
        #    then "carry" the remainder on: subtract space to offset: (offset - spaceBetween).
        #    and continue scanning leftwards.
        # 4. To identify 3., we should encounter a star before actually closing off the current slice.
        # 5. At the end, we scan LTR the string, building a string if its index is not contained in the
        #    slices of indices to delete.

        end = len(s) - 1
        current_slice = [None, None] # (leftmost nonstar, rightmost star)
        owe_stars = False
        slices = deque()     # list of index slices to delete
        
        # Read RTL
        i = end
        while i > -1:
            if s[i] == '*':                     # accumulate stars in slice
                if owe_stars: 
                    nonstars_to_delete += 1
                    print(f"+1 star at {i}, current slice {current_slice} \t (owe {nonstars_to_delete})")
                else:                           # open new index slice          
                    owe_stars = True
                    nonstars_to_delete = 1
                    current_slice[1] = i         # index of rightmost star
                    print(f"First star at {i}, current slice {current_slice} \t (owe {nonstars_to_delete})")
            else:
                # Non-star character
                if owe_stars:
                    nonstars_to_delete -= 1
                    print(f"Rm nonstar {s[i]} at {i} current slice {current_slice} \t (owe {nonstars_to_delete})")
                    
                    if nonstars_to_delete == 0:
                        current_slice[0] = i    # index of leftmost nonstar
                        # Add slice
                        print(f"Owe {nonstars_to_delete}, Closing and adding slice {current_slice}")
                        slices.appendleft(current_slice)

                        # Restart current slice
                        owe_stars = False
                        current_slice = [None, None]
                        print("Restarting slice")
                else:
                    print(f"Nonstar {s[i]} at {i}, ignore")

            i -= 1  # moves left
        print("slices", slices)
        print("Building string next...")

        # Build resulting string
        ans = ''        
        start = 0
        for slice_ in slices:
            stop = slice_[0]
            ans += s[start:stop]
            start = slice_[1] + 1
        # Append remainder of string
        ans += s[start:]
        return ans

# Test
if __name__ == "__main__":
    # st = "lee*tcode*" # "letcod"
    # print(Solution().removeStars(st))
    # print("------------------------------------")
    # st = "erase*****" # ""
    # print(Solution().removeStars(st))
    # print("------------------------------------")
    # st = "leet**cod*e" # "lecoe"
    # print(Solution().removeStars(st))
    # print("------------------------------------")
    # st = "abcdefg*r*ic*****" # "abc"
    # print(Solution().removeStars(st))
    print("------------------------------------")
    st = "acb*a*b*c***" # "abc"
    print(Solution().removeStars(st))
# Prefix starts by definition at index 0 of every string

def longestCommonPrefix(strs):
    # Longest Common Prefix of all strings can be at best as long
    # as the shortest string in the group

    min_len = float('inf')
    for s in strs:
        min_len = min(min_len, len(s))

    lcp = ""

    # for every letter in the first string
    for i in range(min_len):
        # Check if the letter is present in every string
        letter = strs[0][i]

        common = True
        for s in strs:
            # If a string does not share the letter it is not common
            if s[i] != letter:
                common = False
                break

        # If the letter is shared in every string
        if common:
            # add it to the lcp
            lcp += letter
        else:
            break

    return lcp

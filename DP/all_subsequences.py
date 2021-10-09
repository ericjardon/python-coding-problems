# A subsequence is any subset of characters (not necessarily contiguous)
# that appear in order in a string


def allSubsequencesOf(string, subseq = ""):
    '''Recursive approach using a take/not take branching
       Returns a list of all possible subsequences of a string'''
    
    # string is our remaining substring to analyze
    # Any subset of a string is a combination of take/not take decisions until 
    # the string is finished.
    if string == '':
        print(subseq)
        return [subseq]
    
    take = allSubsequencesOf(string[1:], subseq + string[0]) # next char is present
    not_take = allSubsequencesOf(string[1:], subseq)         # next char is NOT present

    # Megre the resulting list of both branches
    return take + not_take


ss = allSubsequencesOf("eric")
print(len(ss))
# Note that if input string has repeated characters, 
# a subset of the subsequences will seem duplicated.
# A total of 2^N subsequences is generated

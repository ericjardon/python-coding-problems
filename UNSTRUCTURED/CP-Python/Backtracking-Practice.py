from typing import List
def letterCasePermutation(S: str) -> List[str]:
    """Given a string S, return all possible derivations from transforming
        any single one of its individual characters. S contains alphanumeric character"""
    ans = set()
    ans.add(S)

    def findPermutations(S:str):
        for i in range(len(S)):
            # produce the lowercase and uppercase derivations
            # using the character at the ith position
            c = S[i]
            if c.isdigit():
                continue
            upper = S[:i] + c.upper() + S[i+1:]
            lower = S[:i] + c.lower() + S[i+1:]
            if upper not in ans:
                ans.add(upper)
                findPermutations(upper)
            if lower not in ans:
                ans.add(lower)
                findPermutations(lower)

    findPermutations(S)

    return list(ans)

## A better solution constructing simultaneously:
def incrementalLCP(S: str) -> List[str]:
    ans = ['']
    for c in S:
        new_ans = []
        for st in ans:
            # At each iteration length of strings increases +1
            # and the num of elements is multiplied by two is c is alpha
            if c.isdigit():
                new_ans.append(st + c)
            else:
                new_ans.append(st + c.lower())
                new_ans.append(st + c.upper())
        ans = new_ans
        # incrementally build the strings in the list
    return ans


def dfs_bt_lcp(S: str) -> List[str]:
    """Recursively builds permutations of S by switching and not the case of alphabetic characters
        and adds them to an outer ans list"""
    ans = []

    def dfs(permutation, i):
        #Base case
        if i == len(S):     # reached end of string
            ans.append(''.join(permutation))
            # reconvert the list to string and add it to answer
            return
        # For every other case i<len(S)
        dfs(permutation, i + 1)      # for character as-is
        if permutation[i].isdigit():
            return      # backtracking condition
        # else, character is alphabetic and can be switched case
        permutation[i] = chr(ord(permutation[i]) ^ 32) # switches lower<->upper and viceversa ^
        # ord() returns integer of character in unicode
        dfs(permutation, i + 1)  # permute with the changed case

    dfs(list(S), 0)
    return ans

## Generate Parentheses
def generateParenthesis(n: int) -> List[str]:
    """Given n pairs of parenthesis, generate and return all possible
    valid combinations of the parentheses"""
    # Rules of the language: has to start (, end with )
    # Number of '(' must equal number of ')'
    # Can put ( or ) as long as open parenthesis > 1 and n>0
    # can only put '
    combinations = set()

    def findComb(n, open, comb):
        # n <- pairs left, open <- number of unpaired (, comb <- string combination
        if n == 0:
            print(comb)
            combinations.add(comb)
        else:
            if open>0:  # if there are still open parenthesis we can close
                findComb(n-1, open-1, comb + ')')   # add )
            if open < n:    # if we can still open another pair
                findComb(n, open+1, comb + '(')     # add (

    findComb(n, 0, '')
    print(list(combinations))

## a faster solution (somehow?)
def fasterParenthesis(n:int) -> List[str]:
    combinations = set()
    if n == 1:
        return ["()"]

    for p in fasterParenthesis(n-1):
        # p is each of the permutations of instance with n-1 pairs
        for i, ch in enumerate(p):
            if ch=='(': # we can also close
                combinations.add(p[:i+1]+"()"+p[i+1:])
            combinations.add(p + "()")
## ??????????????
    return list(combinations)



def main():
    mine = ["((()))()","()()()()","(()())()","()(()())","()((()))","((()()))","(())()()","(((())))","((())())","(()(()))","(()()())","()(())()","()()(())"]
    cpus = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    mine = set(mine)
    cpus = set(cpus)
    print(cpus.difference(mine))

main()
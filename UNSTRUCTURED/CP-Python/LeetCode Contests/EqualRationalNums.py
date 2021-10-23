"""Given strings S and T, representing non-negative rational numbers.
    REturn True if they represent the same number. """


# Rational nums can be separated in <Integer>.<NonRepeating><Repeating>
# The input numbers' repeating part will be enclosed in parenthesis.

# Numbers with periodic .9 must round up.
# Also account for numbers without rational part.
def isRationalEqual(S: str, T: str) -> bool:

    def repeat(baseStr, chars):
        #print("Called repeat: '", baseStr, "' for ", chars)
        if baseStr == "": return "0"*chars
        i = 0
        l = len(baseStr)
        s = ""
        while (chars > 0):
            s += baseStr[i]
            chars -= 1
            i = (i + 1) % l
        #print("repeated string: ", s)
        return s

    parts_S = S.split('.')        # Split into integer.rational parts
    parts_T = T.split('.')
    if parts_S[0] != parts_T[0]:        # compare Integer Part
        return False

    # Integer parts are equal -> Compare rational parts S and T
    if len(parts_S) < 2:  # no rational part
        nonrepS = "0"
        repS = ""
    else:
        rational_parts = parts_S[1].split('(')     # [nonrep, rep)]
        nonrepS = rational_parts[0]
        if len(S) < 2:  # no repeating part
            repS = "0"
        else:
            repS = rational_parts[1][:-1]

    if len(parts_T) < 2:  # no rational part
        nonrepT = "0"
        repT = ""
    else:
        rational_parts = parts_T[1].split('(')
        nonrepT = rational_parts[0]
        if len(T) < 2:      # no repeating part
            repT = ""
        else:
            repT = rational_parts[1][:-1]

    if int(nonrepT+repT) == int(nonrepS+repS):      # handles cases of 0
        return True
    # should handle round-up cases of (9) e.g. 1.0 == 0.(9) is True

    if repT=="" and repS!="" or repT!="" and repS=="":
        return False        # one is infinite and the other isn't, so they can't be the same

    # Paste both repeating and non repeating parts and standardize to max length
    # (the shorter must extend to the larger)
    MAX_RATIONAL_LEN = 8
    S_ = nonrepS + repS
    T_ = nonrepT + repT
    lenS = len(S_)
    lenT = len(T_)
    print("len S:", lenS)
    print("len T:", lenT)
    S_ += repeat(repS, MAX_RATIONAL_LEN - lenS)
    T_ += repeat(repT, MAX_RATIONAL_LEN - lenT)
    print("S:",S_)
    print("T:",T_)
    return S_ == T_

if __name__=="__main__":
    S = "0.52(52)"
    T = "0.525(25)"
    print(isRationalEqual(S,T))
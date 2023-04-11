'''
You are getting a little tired of hunting through some of these so-called “proofs” for the magic tricks that let them prove  and had the great idea to write a computer program to speed things up!
'''

# each line a proof
# assumptions -> conclusion e.g. A, B -> C
# no assumptions then single Axiom e.g.  "-> D"

# proof is valid iff all assumptions where concluded from previous lines

# Previous conclusions can be repeated


# for each line, 0-5 assumptions
# assumptions have an arrow and a conclusion
# assumptions and conclusions are variables of length 1-5

# If every line is correct, output correct
# Otherwise print number of first error


# dictionary for truth

def proof():
    N = int(input()) #lines
    true = {}

    for i in range(N):
        a, c = input().split('->')
        if len(a) > 0:
            asp = a.split()
            for x in asp:
                if x not in true:
                    print(i+1) # line of error
                    return
        # Else, is an Axiom
        true[c[1:]] = True
    
    print("correct")
    return
    
proof()
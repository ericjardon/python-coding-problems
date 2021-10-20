
import string
def caesarCipher(s, k):

    codes = {}
    letters = string.ascii_lowercase
    N = len(letters)

    for i, letter in enumerate(letters):
        codes[letter] = i

    res = ""
    for letter in s:
        letter = letter.lower()
        if letter.isalpha():
            i = (codes[letter] + k) % N

            if letter.isupper():
                res += letters[i].upper()
            else:
                res += letters[i]
        else:
            res += letter
    
    return res

        
s = "middle-Outz"
k = 2
print(caesarCipher(s, k))
'''
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

-----------------
P   A   H   N
A P L S I I G
Y   I   R
-----------------
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            print(s)
            return s
        i = 0
        row = 0
        d = +1
        display = ["" for _ in range(numRows)]
        # while there is characters to append
        while i < len(s):
            print("row", row)
            letter = s[i]
            display[row] += letter
            if row == numRows-1:
                d = -1
            elif row == 0:
                d = +1
            row += d

            i += 1


        ans = ''.join(display)
        print("Ans = ", ans)

Solution().convert("ABC", 2)
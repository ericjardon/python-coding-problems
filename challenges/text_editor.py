class TextEditor():
    def __init__(self) -> None:
        self.s = ''
        self.cache = ['']   # stack

    def append(self, w:str) -> None:
        '''Append a string w to the end of s'''
        self.cache.append(self.s)
        self.s += w
        return

    def delete(self, k:int) -> None:
        '''Delete the last k characters of s'''
        self.cache.append(self.s)
        self.s = self.s[:-k]
        return

    def print(self, k:int) -> None:
        '''Print the kth character of s'''
        print(self.s[k-1])

    def undo(self) -> None:
        '''Return to the previous state'''
        if len(self.cache):
            self.s = self.cache.pop()
            return


if __name__=="__main__":
    """
    Operations:
    1 w -- append
    2 k -- delete last k characters
    3 k -- print kth character
    4 -- undo

    Guaranteed the sequence of operations input is possible
    """
    te = TextEditor()

    for _ in range(int(input())):
        op = input().split()

        if op[0] == '1':
            te.append(op[1])
        
        elif op[0] == '2':
            te.delete(int(op[1]))
        
        elif op[0] == '3':
            te.print(int(op[1]))

        else:
            te.undo()


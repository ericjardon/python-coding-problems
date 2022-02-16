
class TrieNode:
    def __init__(self, w):
        self.w = w
        self.children = {}  # char->TrieNode
        self.isWord = False
            

class Trie:
    
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, word: str) -> None:
        curr = self.root
        match = ""
        for c in word:
            match += c
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        
        #print("inserted word:", match)
        curr.isWord = True
        
        
    def search(self, word: str) -> bool:
        curr = self.root
        match = ""
        for c in word:
            if c not in curr.children:
                #print(word, "not found:", match)
                return False
            match += c
            curr = curr.children[c]
        #print(match, "in Trie, isWord?", curr.isWord)
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        match = ""
        for c in prefix:
            if c not in curr.children:
                #print(prefix, "not found:", match)
                return False
            match += c
            curr = curr.children[c]
        #print(match, "in Trie, is Prefix")
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
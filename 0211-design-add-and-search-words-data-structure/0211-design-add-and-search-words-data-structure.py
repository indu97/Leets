class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}  #char -> Node
            self.is_word = False

    def __init__(self):
        self.root = WordDictionary.Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = WordDictionary.Node()
            curr = curr.children[c]
        curr.is_word = True

    def search_helper(self, w: str, i: int, curr) -> bool:
        n = len(w)
        if i == n:
            return curr.is_word

        c = w[i]

        if c != ".":
            if not c in curr.children:
                return False
            return self.search_helper(w, i+1, curr.children[c])
        else: 
            for key in curr.children:
                if self.search_helper(w, i+1, curr.children[key]): 
                    return True
            return False

        return curr.is_word

    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
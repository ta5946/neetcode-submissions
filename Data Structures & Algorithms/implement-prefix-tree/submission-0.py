class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        current = self.tree
        word += "*"
        for c in word:
            if c not in current.keys():
                current[c] = {}
            current = current[c]

    def search(self, word: str) -> bool:
        word += "*"
        return self.startsWith(word)

    def startsWith(self, prefix: str) -> bool:
        current = self.tree
        for c in prefix:
            if c not in current.keys():
                return False
            current = current[c]
        return True

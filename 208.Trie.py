class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordDict = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.wordDict
        for letter in word:
            if letter not in tree:
                tree[letter] = {}
            tree = tree[letter]
        tree['#'] = '#'


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.wordDict
        for letter in word:
            if letter not in tree:
                return False
            tree = tree[letter]
        if '#' in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.wordDict
        for letter in prefix:
            if letter not in tree:
                return False
            tree = tree[letter]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
"""
211. Add and Search Word - Data structure design
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""
# solution: DFS, time complexity is O(n)
# for adding word, the time complexity is O(n)
# for search word, although recursive searching is used, but the deepth is n at most, so the time complexity is O(n) as well
# n is the length of the word

class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.root
        for w in word:
            if w not in root.children:
                root.children[w] = Trie()
            root = root.children[w]
        root.isWord = True
        root.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return True
        root = self.root
        return self.helper(root, word)

    def helper(self, root, word):
        for i in range(len(word)):
            if word[i] == '.':
                if len(root.children) == 0:
                    return False
                else:
                    for key in root.children.keys():
                        if self.helper(root.children[key], word[i + 1:]):
                            return True
                    return False
            else:
                if word[i] not in root.children:
                    return False
                root = root.children[word[i]]
        return root.isWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
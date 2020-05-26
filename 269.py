"""
Lintcode 892. Alien Dictionary
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.
"""

# solution: time complexity n*m, n is the length of words list; m is the length of each word
from collections import defaultdict


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here
        degree = {}
        for word in words:
            for wor in word:
                if wor not in degree:
                    degree[wor] = 0

        graph = defaultdict(set)

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] == word2[j]:
                    continue
                else:
                    graph[word1[j]].add(word2[j])
                    degree[word2[j]] = degree.get(word2[j], 0) + 1
                    break

        stack = []
        for key, value in degree.items():
            if value == 0:
                stack.append(key)

        stack.sort()

        res = ''
        while stack:
            cur = stack.pop(0)
            res += cur
            if cur in graph:
                for nei in graph[cur]:
                    degree[nei] -= 1
                    if degree[nei] == 0:
                        stack.append(nei)

            stack.sort()

        if len(res) == len(degree):
            return res
        return ''

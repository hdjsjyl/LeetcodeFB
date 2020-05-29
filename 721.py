"""
721. Accounts Merge
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
"""

# solution: union find, time complexity: O(n*m)
# n is the number of accounts in the accounts array; m is the number of emails of each account

from collections import defaultdict


class Solution:
    def __init__(self):
        self.fathers = {}

    def find(self, a):
        path = []
        while a != self.fathers[a]:
            path.append(a)
            a = self.fathers[a]

        for i in path:
            self.fathers[i] = a

        return a

    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.fathers[fa] = fb

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        for i in range(len(accounts)):
            self.fathers[i] = i

        emails_to_ids = defaultdict(set)
        for idx, acc in enumerate(accounts):
            for a in acc[1:]:
                emails_to_ids[a].add(idx)

        for key, value in emails_to_ids.items():
            if len(value) == 1:
                continue
            else:
                vals = list(value)
                f0 = self.find(vals[0])
                for val in vals[1:]:
                    self.union(f0, val)

        res_dicts = defaultdict(set)
        for idx, acc in enumerate(accounts):
            fidx = self.find(idx)
            for ac in acc[1:]:
                res_dicts[fidx].add(ac)

        res = []
        for key, value in res_dicts.items():
            tmp = []
            tmp.append(accounts[key][0])
            tmp += list(value)
            tmp.sort()
            res.append(tmp)

        return res

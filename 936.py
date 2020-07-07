"""
936. Stamping The Sequence
Hard

177

51

Add to List

Share
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.



Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)
"""

## TC: O(nnm)

## from the last to step to previous step to match the string
class Solution(object):
    def check(self, s, t):
        for i in range(len(t)):
            if t[i] == '?':
                continue
            if t[i] != s[i]:
                return False
        return True

    def check2(self, s, t, i, j):
        p = 0
        for k in range(i, j):
            if t[k] == '?':
                p += 1
                continue
            if t[k] != s[p]:
                return False
            p += 1
        return True

    def movesToStamp(self, s, target):
        m = len(s)
        n = len(target)
        turn = 0
        compare = '?' * m
        res = []
        while turn < 10 * n:
            tmp = turn
            for i in range(n - m + 1):
                # if target[i:i+m] != compare and self.check(s, target[i:i+m]):
                if target[i:i + m] != compare and self.check2(s, target, i, i + m):
                    turn += 1
                    res.append(i)
                    target = target[:i] + compare + target[i + m:]

            if target == '?' * n:
                return res[::-1]

            if turn == tmp:
                break
        return []

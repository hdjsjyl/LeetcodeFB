"""
lintcode: 660. Read N Characters Given Read4 II - Call multiple times
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Example
Example 1

Input:
"filetestbuffer"
read(6)
read(5)
read(4)
read(3)
read(2)
read(1)
read(10)
Output:
6, buf = "filete"
5, buf = "stbuf"
3, buf = "fer"
0, buf = ""
0, buf = ""
0, buf = ""
0, buf = ""
"""

# solution
# idea1: considering the condition that we didn't pick out all elements in the buff
# this time, we need to pick up the rest of the elements firstly, so we need a start index, and an end index
# to get which elements we need to pick up
# idea2: each time, we need to make sure, whether there are elements to be picked up for next time; so we need
# a flag to check whether we already pick up all the elements. If yes, for the following times, we just return 0
"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:

    def __init__(self):
        self.buff = [None for i in range(4)]
        self.idx = -1
        self.end = -1
        self.f = False

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        if self.f:
            return 0
        j = 0
        if self.idx != -1:
            for i in range(self.idx, self.end):
                buf[j] = self.buff[i]
                j += 1
            if self.end < 4:
                self.f = True
                return j

        c1 = (n - j) % 4
        c2 = (n - j) // 4
        for i in range(c2):
            tmp = Reader.read4(self.buff)
            for p in range(tmp):
                buf[j] = self.buff[p]
                j += 1
            if tmp < 4:
                self.f = True
                return j

        tmp = Reader.read4(self.buff)
        if tmp <= c1:
            self.f = True
            for i in range(tmp):
                buf[j] = self.buff[i]
                j += 1
            return j
        else:
            for i in range(c1):
                buf[j] = self.buff[i]
                j += 1
            self.idx = c1
            self.end = tmp
            return j
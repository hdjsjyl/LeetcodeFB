"""
65. Valid Number
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""

# solution: for mathmetics problem, considering the corner cases;
# considering the conditions which include '.', 'e'
# time complexity: O(n)
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        i = 0
        k = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return False
        if s[i] == '+' or s[i] == '-':
            i += 1
        if i == len(s):
            return False
        while i < len(s) and s[i].isdigit():
            i += 1
            k += 1
        if i == len(s):
            return True
        if s[i] == '.':
            i += 1
        if i == len(s) and k > 0:
            return True
        elif i == len(s) and k == 0:
            return False
        while i < len(s) and s[i].isdigit():
            i += 1
            k += 1
        if k == 0:
            return False
        if i == len(s):
            return True
        if s[i] == 'e':
            if k == 0:
                return False
            k = 0
            i += 1
            if i == len(s):
                return False
            if s[i] == '-' or s[i] == '+':
                i += 1
            while i < len(s) and s[i].isdigit():
                i += 1
                k += 1
            if k == 0:
                return False
        while i < len(s) and s[i] == ' ':
            i += 1
        return i == len(s)
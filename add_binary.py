#05:51 -> 06:22
"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_l = list(a)
        b_l = list(b)
        diff = len(a_l) - len(b_l)

        if diff > 0:
            b_l = ['0'] * abs(diff) + b_l
        elif diff < 0:
            a_l = ['0'] * abs(diff) + a_l

        final_res = ''
        rem = 0

        for index in range(len(a_l) - 1, -1, -1):
            temp_res, rem = self.helper(int(a_l[index]) + int(b_l[index]) + rem)
            final_res = temp_res + final_res

        if rem == 1:
            final_res = '1' + final_res

        return final_res

    def helper(self, val):
        if val == 0:
            return '0', 0
        elif val == 1:
            return '1', 0
        elif val == 2:
            return '0', 1
        elif val == 3:
            return '1', 1
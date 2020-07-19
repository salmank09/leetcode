import math

"""
Attempt 1: 10:27, 9 min
Attempt 2: 3:10, 4:16, 66 min #Attempted by determining digit count of input via string conversion
TODO: Review top solutions

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

Total Time: 9 min
"""
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        y = 0
        num_digits = int(math.log10(x))+1
        is_even = num_digits % 2 == 0
        while True:
            y = y*10 + x % 10
            if is_even:
                x = x/10
                if y > x:
                    return False
                elif y == x:
                    return True
            else:
                if y > x:
                    return False
                elif y == x:
                    return True
                x = x/10

obj = Solution()

print(obj.isPalindrome(121) == True)

print(obj.isPalindrome(122) == False)

print(obj.isPalindrome(1221) == True)

print(obj.isPalindrome(12221) == True)

print(obj.isPalindrome(0) == True)

print(obj.isPalindrome(12) == False)
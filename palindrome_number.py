"""
Problem:
Given an integer x, return true if x is a palindrome , and false otherwise.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Source: leetcode.com
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)[:]



"""
Imperative method:
 class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = x
        reverse = 0

        while number != 0:
            last_digit = number % 10
            reverse = reverse * 10 + last_digit
            number //= 10

        return x == reverse
 """  
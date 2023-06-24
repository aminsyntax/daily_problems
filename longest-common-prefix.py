"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Source: leetcode.com
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        first_str = strs[0]
        last_str = strs[-1]
        prefix = ""

        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                prefix += first_str[i]
            else:
                break
        
        return prefix


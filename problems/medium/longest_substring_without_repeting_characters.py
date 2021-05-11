'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

link -> https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def length_of_longest_substring(self, s: str) -> int:

        left = 0
        right = 0
        mem = {}
        max_len = 0
        while left < len(s) and right < len(s):
            if mem is None or s[right] not in mem:
                mem[s[right]] = right
                length = right - left + 1
                if length > max_len:
                    max_len = length
                right = right + 1
            elif mem is not None and mem[s[right]] is not None:
                left = mem[s[right]] + 1
                right = left
                mem = {}
        return max_len


if __name__ == "__main__":
    solution = Solution()
    result = solution.length_of_longest_substring("pwwkew")
    print(result)
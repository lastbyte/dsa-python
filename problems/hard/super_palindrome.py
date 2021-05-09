'''
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

 

Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
Example 2:

Input: left = "1", right = "2"
Output: 1
 

Constraints:

1 <= left.length, right.length <= 18
left and right consist of only digits.
left and right cannot have leading zeros.
left and right represent integers in the range [1, 1018].
left is less than or equal to right.

link -> https://leetcode.com/problems/super-palindromes/
'''


class Solution:
    def super_palindromes_in_range(self, left, right):
        i = int(pow(int(left), 1 / 2))
        u_bound = int(pow(int(right), 1 / 2))
        count = 0
        while i <= u_bound:
            if self.is_palindrome(str(i)) and self.is_palindrome(str(i * i)):
                count += 1
            i = int(self.find_next_smallest_palindrome(str(i)))
        return count

    def find_next_smallest_palindrome(self, n):
        l = len(n)

        if self.contains_only_nine(n):
            return str(int(n) + 2)

        if self.is_palindrome(n):
            return self.increment_to_next_palindrome(n)
        else:
            left, right = n[0:l // 2][::-1], n[-(l // 2):]
            if left > right:
                return self.convert_into_palindrome(n)
            else:
                return self.increment_to_next_palindrome(
                    self.convert_into_palindrome(n))

    def convert_into_palindrome(self, num):
        l = len(num)
        if l % 2 == 0:
            left = num[0:l // 2]
            return left + left[::-1]
        else:
            left = num[0:l // 2 + 1]
            return left + left[::-1][1:]

    def increment_to_next_palindrome(self, num):
        l = len(num)
        if l % 2 == 0:
            left = str(int(num[0:l // 2]) + 1)
            return left + left[::-1]
        else:
            left = str(int(num[0:l // 2 + 1]) + 1)
            return left + left[::-1][1:]

    def contains_only_nine(self, num):
        for i in num:
            if i != '9':
                return False
        return True

    def is_palindrome(self, n):
        for i in range(len(n) // 2):
            if n[i] != n[len(n) - i - 1]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    result = solution.super_palindromes_in_range("40000000000000000",
                                                 "50000000000000000")
    print(result)
'''
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].

link -> https://leetcode.com/problems/find-the-closest-palindrome/
'''


class Solution():
    def find_closest_palindrome(self, n):
        n1 = n[:]
        n2 = n[:]
        prev_largest = self.find_prev_largest_palindrome(n1)
        next_smallest = self.find_next_smallest_palindrome(n2)

        diff1 = abs(int(prev_largest) - int(n))
        diff2 = abs(int(next_smallest) - int(n))

        if diff1 <= diff2:
            return prev_largest
        else:
            return next_smallest

    def find_next_smallest_palindrome(self, n):
        l = len(n)
        matches_pattern = self.is_match(n)
        if matches_pattern:
            return str(10**matches_pattern-1)
        if self.contains_only_nine(n):
            return str(int(n) + 2)

        if self.is_palindrome(n):
            return self.increment_to_next_palindrome(n)
        else:
            left,right = n[0:l//2][::-1],n[-(l//2):]
            if left > right:
                return self.convert_into_palindrome(n)
            else:
                return self.increment_to_next_palindrome(self.convert_into_palindrome(n))

    def find_prev_largest_palindrome(self, n):
        l = len(n)

        if self.is_palindrome(n):
            return self.decrement_to_next_palindrome(n)
        else:
            left, right = n[0:l // 2][::-1], n[-(l // 2):]
            if left < right:
                return self.convert_into_palindrome(n)
            else:
                return self.decrement_to_next_palindrome(
                    self.convert_into_palindrome(n))

    def convert_into_palindrome(self,num):
        l = len(num)
        if l % 2 == 0:
            left = num[0:l // 2]
            return left + left[::-1]
        else:
            left = num[0:l // 2 + 1]
            return left + left[::-1][1:]

    def increment_to_next_palindrome(self,num):
        l = len(num)
        if l%2 == 0:
            left = str(int(num[0:l//2]) + 1)
            return left + left[::-1]
        else:
            left = str(int(num[0:l // 2 + 1]) + 1)
            return left + left[::-1][1:]

    def decrement_to_next_palindrome(self, num):
        l = len(num)
        if l % 2 == 0:
            left = str(int(num[0:l // 2]) - 1)
            return left + left[::-1]
        else:
            left = str(int(num[0:l // 2 + 1]) - 1)
            return left + left[::-1][1:]

    def is_palindrome(self, n):
        for i in range(len(n) // 2):
            if n[i] != n[len(n) - i - 1]:
                return False
        return True

    def contains_only_nine(self,num):
        for i in num:
            if i != '9':
                return False
        return True

    def is_match(self, num):
        n = int(num)
        i,x = 0,1
        while x <= n:
            if x == n or x+1 == n:
                return i
            i+=1
            x=10**i
        return False

if __name__ == "__main__":
    solution = Solution()
    result = solution.find_closest_palindrome("123892133")
    print(result)

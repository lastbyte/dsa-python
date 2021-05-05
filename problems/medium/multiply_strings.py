'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.


link -> https://leetcode.com/problems/multiply-strings/
'''

def multiply_strings(s1,s2):
    return str(string_to_number(s1) * string_to_number(s2))

def string_to_number(s):
    num = 0
    for i in range(len(s)): num += ((10**i) * (ord(s[len(s)-i-1]) - ord('0')))
    return num


num1 = "123"
num2 = "456"

result = multiply_strings(num1, num2)
print(result)

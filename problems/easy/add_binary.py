'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

link -> https://leetcode.com/problems/add-binary/
'''
class Solution:
    def add_binary(self, a, b):
        index_a = 0
        index_b = 0
        ans = ''
        al = len(a)
        bl = len(b)
        carry = '0'
        bin_map = {
            '000' : ['0','0'],
            '001' : ['1','0'],
            '010' : ['1','0'],
            '011' : ['0','1'],
            '100' : ['1','0'],
            '101' : ['0','1'],
            '110' : ['0','1'],
            '111' : ['1','1'],
        }
        while index_a < al and index_b < bl:
            entry = bin_map[carry+a[al-index_a-1]+b[bl-index_b-1]]
            carry = entry[1]
            ans = entry[0] + ans
            index_a+=1
            index_b+=1


        while index_a < al:
            entry = bin_map[carry + a[al - index_a - 1] + '0']
            carry = entry[1]
            ans = entry[0] + ans
            index_a += 1

        while index_b < bl :
            entry = bin_map[carry + '0' + b[bl - index_b - 1]]
            carry = entry[1]
            ans = entry[0] + ans
            index_b += 1

        if carry == '1':
            ans = carry + ans
        return ans


if __name__ == "__main__":
    solution = Solution()
    result = solution.add_binary("1010", "1011")
    print(result)
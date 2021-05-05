'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8
 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. 
For this problem,assume that your function returns 231 − 1 when the division result overflows.
'''


class Solution:
    def divide(self, dividend, divisor):
        negative = False
        found = False
        quotient = 1
        if dividend < 0: negative, dividend = not negative, abs(dividend)

        if divisor < 0: negative, divisor = not negative, abs(divisor)

        if dividend < divisor or dividend == 0:
            return 0

        if divisor == 1:
            quotient, found = dividend, True

        divisor_copy = divisor

        while divisor_copy << 1 < dividend and not found:
            divisor_copy, quotient = divisor_copy << 1, quotient << 1

        if dividend - divisor_copy >= divisor and not found:
            quotient += self.divide(dividend - divisor_copy, divisor)

        quotient = quotient if not negative else -quotient
        return quotient if quotient <= 2**31 - 1 else 2**31 - 1


print(Solution().divide(10, 3))
print(Solution().divide(7, 3))
print(Solution().divide(7, -3))
print(Solution().divide(0, 1))
print(Solution().divide(9999999999999999, 7))
print(Solution().divide(-2147483648, -1))
print(Solution().divide(-2147483648, 1))
print(Solution().divide(-231, 3))

print(9999999999999999 // 7)

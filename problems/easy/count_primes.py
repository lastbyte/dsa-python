'''
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 10^6

link -> https://leetcode.com/problems/count-primes/

'''


class Solution:
    def count_primes(self, n):
        mem_arr = [i for i in range(0, n)]
        u_bound = int(pow(n, 1 / 2))
        for i in range(2, u_bound + 1):
            if mem_arr[i] < 0:
                continue
            for j in range(i * i, len(mem_arr), i):
                if mem_arr[j] % i == 0:
                    mem_arr[j] = -abs(mem_arr[j])
        return len([i for i in mem_arr if i > 1])


if __name__ == "__main__":
    solution = Solution()
    result = solution.count_primes(10000)
    print(result)
'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

link -> https://leetcode.com/problems/climbing-stairs/
'''


from typing import List


class Solution:
    def climbing_stairs(self, n):
        mem = [0] * (n + 1)
        return self.climbing_stairs_util(n,mem)

    def climbing_stairs_util(self, n:int, mem:List[int]):
        if n == 1 :
            mem[1] = 1
            return mem[1]
        elif n ==2:
            mem[2] = 2
            return mem[2]
        elif mem[n] != 0:
            return mem[n]
        else:
            mem[n] = self.climbing_stairs_util(n-1, mem) + self.climbing_stairs_util(n-2,mem)
            return mem[n]


if __name__ == "__main__":
    solution = Solution()
    result = solution.climbing_stairs(38)
    print(result)


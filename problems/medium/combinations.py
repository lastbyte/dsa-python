'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.


Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]

Constraints:

1 <= n <= 20
1 <= k <= n

link -> https://leetcode.com/problems/combinations/

'''

class Solution:

    def combinations(self, n, k):
        nums = [ i for i in range(1, n+1)]
        total_combinations = []
        for i in range(n):
            self.combinationsUtil(nums[i+1:], [nums[i]], total_combinations, k-1)
        return total_combinations

    def combinationsUtil(self, nums,combination, total_combination, k):
        if k==0:
            total_combination.append(combination.copy())
        else:
            for i in range(len(nums)):
                combination.append(nums[i])
                self.combinationsUtil(nums[i+1:], combination, total_combination, k-1)
                combination.pop()




if __name__ == "__main__":
    solution = Solution()
    result = solution.combinations(4,2)
    print(result)

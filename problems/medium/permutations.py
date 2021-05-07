'''

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


'''
class Solution:

    def generate_permutations(self,nums):
        permutations=[]
        self.generate_permutations_util(nums,0, len(nums)-1,permutations)
        return permutations


    def generate_permutations_util(self,nums,left, right, permutations):
        if left == right:
            permutations.append(nums.copy())
        for i in range(left, right+1):
            nums[left], nums[i] = nums[i], nums[left]
            self.generate_permutations_util(nums, left+1, right, permutations)
            nums[left], nums[i] = nums[i], nums[left]


if __name__ == "__main__":
    permutations = []
    nums=[1,1,3]
    solution = Solution()
    result = solution.generate_permutations(nums)
    print(result)

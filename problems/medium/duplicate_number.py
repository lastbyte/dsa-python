'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1
 
Constraints:

2 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

link -> https://leetcode.com/problems/find-the-duplicate-number/
'''

def find_duplicate(nums):
        for i in range(len(nums)):
            index = abs(nums[i])
            if nums[index] < 0:
                return index
            else:
                nums[index] = -nums[index]
        return -1

if __name__ =="__main__":
    nums = [1, 1, 2]
    result = find_duplicate(nums)
    print(result)
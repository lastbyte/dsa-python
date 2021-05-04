'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:


Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

source -> https://leetcode.com/problems/non-decreasing-array/
'''


def non_descreasing_array(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if i == 1 or nums[i - 2] <= nums[i]:
                nums[i - 1] = nums[i]
                count += 1
            else:
                nums[i] = nums[i - 1]
                count += 1
    return count <= 1


if __name__ == "__main__":
    nums = [4, 2, 3]
    result = non_descreasing_array(nums)
    print("nums : {} , result : {}".format(nums, result))

    nums = [4, 2, 1]
    result = non_descreasing_array(nums)
    print("nums : {} , result : {}".format(nums, result))

    nums = [5, 7, 1, 8]
    result = non_descreasing_array(nums)
    print("nums : {} , result : {}".format(nums, result))
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
link -> https://leetcode.com/problems/combination-sum-ii/
'''


def combination_sum(nums, target):
    combinations = []
    nums.sort()
    combination_sum_util(nums, 0, target, combinations, [])
    return combinations


def combination_sum_util(nums, start, target, combinations,
                         current_combination):
    if target == 0:
        copy_current_combination = current_combination.copy()
        combinations.append(copy_current_combination)
        current_combination = []
    elif target > 0 and start < len(nums):
        copy_current_combination = current_combination.copy()
        copy_current_combination.append(nums[start])
        combination_sum_util(nums, start + 1, target - nums[start],
                             combinations, copy_current_combination)
        copy_current_combination = current_combination.copy()
        start+=1
        while start < len(nums) and nums[start] == nums[start-1]:
            start+=1
        combination_sum_util(nums, start, target, combinations,
                                    copy_current_combination)


if __name__ == "__main__":
    nums = [10, 1, 2, 7, 6, 1, 5] # 1,1,2,5,6,7,10
    target = 8
    result = combination_sum(nums, target)
    print(result)

    nums = [2, 5, 2, 1, 2]
    target = 5
    result = combination_sum(nums, target)
    print(result)

    nums = [3,1,3,5,1,1] # 1,1,1,3,3,5
    target = 8
    result = combination_sum(nums, target)
    print(result)

    nums = [1] * 28# 1,1,1,3,3,5
    target = 27
    result = combination_sum(nums, target)
    print(result)

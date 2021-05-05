'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations 
of candidates where the chosen numbers sum to target. You may return the combinations in any order.The same number
may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least
one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the 
given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]

link -> https://leetcode.com/problems/combination-sum/
'''


def combination_sum(nums, target):
    combinations = []
    combination_sum_util(nums,0,target,combinations, [])
    return combinations


def combination_sum_util(nums, start, target, combinations,
                         current_combination):
    if target == 0:
        combinations.append(current_combination.copy())
        current_combination=[]
    elif target > 0 :
        copy_current_combination = current_combination.copy()
        copy_current_combination.append(nums[start])
        combination_sum_util(nums, start, target-nums[start],combinations,copy_current_combination)
        if start+1 < len(nums):
            copy_current_combination = current_combination.copy()
            combination_sum_util(nums, start+1,target, combinations, copy_current_combination)




if __name__ == "__main__":
    nums = [2,3,6,7]
    target = 7
    result = combination_sum(nums,target)
    print(result)

    nums = [1]
    target = 1
    result = combination_sum(nums,target)
    print(result)

    nums = [2, 3, 5]
    target = 8
    result = combination_sum(nums,target)
    print(result)

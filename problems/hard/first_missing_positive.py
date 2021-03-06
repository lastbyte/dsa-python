'''

Given an unsorted integer array nums, find the smallest missing positive integer.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space?

link -> https://leetcode.com/problems/first-missing-positive/
'''


def first_missing_positive(nums):
    smallest_positive = 1
    nums.sort()
    for i in range(size):
        if nums[i] == smallest_positive:
            smallest_positive += 1
    return smallest_positive


def first_missing_positive_1(nums):
    size = len(nums)
    if 1 not in nums:
        return 1   
    
    if size == 1:
        return 2
     
    for i in range(size):
        if nums[i] <= 0 or nums[i] > size: nums[i] = 1

    for i in range(size):
        index = abs(nums[i])
        if index == size :
            nums[0] = - abs(nums[0])
        else:
            nums[index] = - abs(nums[index])
    
    for i in range(1,size):
        if nums[i] > 0 : return i
    
    return size if nums[0] > 0 else size+1


if __name__ == "__main__":
    nums = [2, 2, 6, 5, 4, 3, 8, 1]
    result = first_missing_positive_1(nums)
    print(result)

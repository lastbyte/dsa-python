'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

link -> https://leetcode.com/problems/two-sum/
'''


class Solution:
    def get_key(self, obj):
        return obj['val']

    def two_sum(self, nums, target):
        num_pos = []
        for idx, val in enumerate(nums):
            num_pos.append({"val": val, "idx": idx})

        num_pos.sort(key=self.get_key)

        left, right = 0, len(nums) - 1

        while left < right and left < len(nums) and right >= 0:
            if num_pos[left]["val"] + num_pos[right]["val"] == target:
                return [num_pos[left]["idx"], num_pos[right]["idx"]]
            elif num_pos[left]["val"] + num_pos[right]["val"] < target:
                left += 1
            else:
                right -= 1

    '''
    Explanation :- 
        kepp a track of nums visited with their index in a map while moving them
        to the next element chekck if (target- num) is present in the map is present in
        return both the indexes
    
    Time Complexity :- 
        Best Case :  O(n)
        Average Case :  O(n)
        Worst Case :  O(n)
    
    Space Complexity :- 
        Best Case :  O(n)
        Average Case : O(n)
        Worst Case : O(n)
    '''

    def two_sum_1(self, nums, target):
        inv_map = {}
        for index, num in enumerate(nums):
            num_inverse_index = inv_map.get(target - num)
            if num_inverse_index is not None:
                return [num_inverse_index, index]
            else:
                inv_map[num] = index


if __name__ == "__main__":
    solution = Solution()
    result = solution.two_sum_1([3, 2, 4], 6)
    print(result)
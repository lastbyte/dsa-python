'''

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105

link -> https://leetcode.com/problems/jump-game/
'''


def canJump(nums):
    farthest = 0
    current_pos = 0

    while current_pos <= farthest:
        farthest = max(farthest, current_pos + nums[current_pos])
        if farthest >= len(nums) - 1:
            return True
        current_pos += 1

    return False

    def test_can_jumps():
        assert (canJump([2, 3, 1, 1, 4]) == True)


if __name__ == "__main__":
    result = canJump([2, 3, 1, 1, 4])
    print(result)
    result = canJump([3, 2, 1, 0, 4])
    print(result)
    result = canJump([1, 2, 3])
    print(result)
    result = canJump([3, 0, 8, 2, 0, 0, 1])
    print(result)

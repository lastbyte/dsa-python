'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.
'''


class Solution:
    def min_jumps(self, nums):
        min_jumps_at = [-1] * len(nums)
        return self.min_jumps_util(nums, 0, len(nums)-1, min_jumps_at)

    def min_jumps_util(self, nums, pos, tar, min_jumps_at):

        if min_jumps_at[pos] != -1:
            return min_jumps_at[pos]
        if pos == len(nums) - 1:
            return 0

        if nums[pos] == 0:
            return float('inf')

        min_jump = float('inf')

        for i in range(pos + 1, tar + 1):
            if (i < pos + nums[pos] + 1):
                jumps = self.min_jumps_util(nums, i, tar, min_jumps_at)
                if (jumps != float('inf') and jumps + 1 < min_jump):
                    min_jump = jumps + 1
        min_jumps_at[pos] = min_jump
        return min_jump


if __name__ == "__main__":
    #nums = [2,3,1,1,4]
    nums = [
        5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7,
        9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5
    ]
    solution = Solution()
    result = solution.min_jumps(nums)
    print(result)
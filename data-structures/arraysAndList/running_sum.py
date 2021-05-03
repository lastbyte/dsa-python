'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''


class Solution:
    def running_sums(self, nums):
        running_sums = []
        for index, num in enumerate(nums):
            if index == 0:
                running_sums.append(num)
            else:
                running_sums.append(running_sums[index - 1] + num)
        return running_sums


nums = [3, 1, 2, 10, 1]
result = Solution().running_sums(nums)
print(result)

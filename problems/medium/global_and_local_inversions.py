'''
You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

The number of global inversions is the number of the different pairs (i, j) where:

0 <= i < j < n
nums[i] > nums[j]
The number of local inversions is the number of indices i where:

0 <= i < n - 1
nums[i] > nums[i + 1]
Return true if the number of global inversions is equal to the number of local inversions.

 

Example 1:

Input: nums = [1,0,2]
Output: true
Explanation: There is 1 global inversion and 1 local inversion.
Example 2:

Input: nums = [1,2,0]
Output: false
Explanation: There are 2 global inversions and 1 local inversion.

link -> https://leetcode.com/problems/global-and-local-inversions/
'''


class Solution:
    def is_global_and_local_equal(self, nums):
        global_inversions = self.count_global_inversions(nums.copy(), 0, len(nums) - 1)
        local_inversions = self.count_local_inversions(nums)
        return global_inversions == local_inversions

    def count_local_inversions(self, nums):
        local_inversions = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                local_inversions += 1
        return local_inversions

    def count_global_inversions(self, nums, start, end):
        count = 0
        if (start < end):
            mid = (end + start) // 2
            count += self.count_global_inversions(nums, start, mid)
            count += self.count_global_inversions(nums, mid + 1, end)
            count += self.merge(nums, start, mid, end)
        return count

    def merge(self, nums, start, mid, end):
        tmp = []

        i, j, count = start, mid + 1, 0

        while i <= mid and j <= end:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                count += (mid - i + 1)
                j += 1

        if i <= mid:
            tmp = tmp + nums[i:mid + 1]
        if j <= end:
            tmp = tmp + nums[j:end + 1]

        for i in range(len(tmp)):
            nums[start + i] = tmp[i]
        return count


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 0, 2]
    result = solution.is_global_and_local_equal(nums)
    print(result)
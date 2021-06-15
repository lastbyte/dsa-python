'''
Implement next permutation, which rearranges nums into the lexicographically next greater permutation of numss.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

link -> https://leetcode.com/problems/next-permutation/
'''


class Solution:
    def next_permutation(self, nums):
        n = len(nums)
        if n == 1:
            return
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                break

        if i == 1 and nums[i] <= nums[i - 1]:
            nums.sort()
            return

        x = nums[i - 1]
        smallest = i
        for j in range(i + 1, n):
            if nums[j] > x and nums[j] < nums[smallest]:
                smallest = j

        nums[smallest], nums[i - 1] = nums[i - 1], nums[smallest]

        self.quicksort(nums, i, len(nums) - 1)

    def quicksort(self, array, left, right):
        if left < right:
            pivot = self.partition(array, left, right)
            self.quicksort(array, left, pivot - 1)
            self.quicksort(array, pivot + 1, right)

    def partition(self, array, left, right):
        pivot = left
        correct_pivot = left

        for i in range(left, right + 1):
            if array[i] < array[pivot]:
                correct_pivot = correct_pivot + 1
                array[i], array[correct_pivot] = array[correct_pivot], array[i]

        array[correct_pivot], array[pivot] = array[pivot], array[correct_pivot]
        return correct_pivot


# nums = [3, 2, 1]
nums = [1, 3, 2]
# nums = [2,3,1,3,3]
result = Solution().next_permutation(nums)
print(nums)
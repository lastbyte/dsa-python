'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!

link -> https://leetcode.com/problems/permutation-sequence/
'''


class Solution:
    def permutation_sequence(self, n, k):
        nums = [i for i in range(1, n + 1)]
        for i in range(k - 1):
            self.next_permutation(nums)
        return ''.join(map(str, nums))

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

    def permutation_sequence_1(self, n, k):
        nums = [i for i in range(1, n + 1)]
        sequence = []
        for i in range(n):
            u_bound = self.factorial(n - i - 1)
            count = 0
            while k > u_bound:
                k -= u_bound
                count += 1
            sequence.append(nums.pop(count))
            if k == 0:
                break

        sequence = sequence + nums[i:]

        return ''.join(map(str, sequence))

    def factorial(self, n):
        return 1 if n == 0 else n * self.factorial(n - 1)


if __name__ == "__main__":
    solution = Solution()
    result = solution.permutation_sequence(3, 3)
    result = solution.permutation_sequence_1(3, 3)
    print(result)
'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
link -> https://leetcode.com/problems/kth-largest-element-in-an-array/
'''


class Solution:
    def kth_largest(self, arr, k):
        heap = []
        for i in range(k):
            heap.append(arr[i])

        self.min_heapify(heap, 0)
        kth = heap[0]
        for i in range(k, len(arr)):
            kth = heap[0]
            if arr[i] > kth:
                heap.pop(0)
                heap.append(arr[i])
                self.min_heapify(heap, 0)

        return heap[0]

    def min_heapify(self, arr, index):
        if arr is None:
            return

        left = index * 2 + 1
        right = index * 2 + 2

        if left < len(arr):
            self.min_heapify(arr, left)

        if right < len(arr):
            self.min_heapify(arr, right)

        if left < len(arr) and arr[index] > arr[left]:
            arr[index], arr[left] = arr[left], arr[index]

        if right < len(arr) and arr[index] > arr[right]:
            arr[index], arr[right], = arr[right], arr[index]


if __name__ == "__main__":
    sol = Solution()
    result = sol.kth_largest([6, 9, 3, 4, 5, 10, 7, 8, 2], 3)
    print(result)

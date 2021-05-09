'''
Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

Examples:  

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 4 
Output: 10 

link -> https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

'''


class Solution:
    def kth_smallest(self, arr, k):
        heap = []
        for i in range(k):
            heap.append(arr[i])

        self.max_heapify(heap, 0)
        kth = heap[0]
        for i in range(k, len(arr)):
            kth = heap[0]
            if arr[i] < kth:
                heap.pop(0)
                heap.append(arr[i])
                self.max_heapify(heap, 0)
        return heap[0]

    def max_heapify(self, arr, index):
        if arr is None:
            return

        left = index * 2 + 1
        right = index * 2 + 2

        if left < len(arr):
            self.max_heapify(arr, left)

        if right < len(arr):
            self.max_heapify(arr, right)

        if left < len(arr) and arr[index] < arr[left]:
            arr[index], arr[left] = arr[left], arr[index]

        if right < len(arr) and arr[index] < arr[right]:
            arr[index], arr[right], = arr[right], arr[index]


if __name__ == "__main__":
    sol = Solution()
    result = sol.kth_smallest([6, 9, 3, 4, 5, 10, 7, 8, 2], 3)
    print(result)
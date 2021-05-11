'''
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

 

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true
 

Constraints:

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9

link -> https://leetcode.com/problems/construct-target-array-with-multiple-sums/
'''

class Solution:
    def is_target_sum_possible(self,target):
        if len(target) == 1 : return target == [1]
        self.max_heapify(target, 0)
        total = sum(target)
        while target[0] > 1:
            elem = target[0]
            rest_sum = total - elem
            if rest_sum == 1:
                return True
            new_elem = elem % rest_sum
            if new_elem == 0 or elem == new_elem :
                return False
            total = total - elem + new_elem
            target.pop(0)
            target.insert(0, new_elem)
            self.max_heapify(target, 0)
        return True


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
    solution = Solution()
    result = solution.is_target_sum_possible([1, 1, 85, 13, 43, 1, 1])
    print(result)
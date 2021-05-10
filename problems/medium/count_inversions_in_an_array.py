'''
Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
If the array is already sorted, then the inversion count is 0, but if the array is sorted 
in the reverse order, the inversion count is the maximum. Formally speaking, two elements 
a[i] and a[j] form an inversion if a[i] > a[j] and i < j 

Example: 

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).


Input: arr[] = {3, 1, 2}
Output: 2

Explanation: Given array has two inversions:
(3, 1), (3, 2) 

link -> https://www.geeksforgeeks.org/counting-inversions/
'''


class Solution:
    '''
    Explanation :- 
        brute force approck is to check for all the pairs and return the count 
    
    Time Complexity :- 
        Best Case : O(n) 
        Average Case : O(n^2) 
        Worst Case :  O(n^2)
    
    Space Complexity :- 
        Best Case :  O(1)
        Average Case : O(1)
        Worst Case : O(1)
    '''
    def count_inversions_0(self, nums):
        count = 0
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                if i < j and nums[i] > nums[j]:
                    count += 1
        return count

    '''
    Explanation :- 
        total number of inversions in an array will be equal to the number
        of inversions in left half of the array plus the number of inversion
        in the right half of the array plus the number of inversions needed
        to merge the  left and right part together. 
    
    Time Complexity :- 
        Best Case :  O(n)
        Average Case :  O(nlogn)
        Worst Case :   O(nlogn)
    
    Space Complexity :- 
        Best Case :  O(n)
        Average Case : O(n)
        Worst Case : O(n)
    '''
    def count_inversions_1(self, nums):
        return self.modified_merge_sort(nums, 0, len(nums) - 1)

    def modified_merge_sort(self, nums, start, end):
        count = 0
        if (start < end):
            mid = (end + start) // 2
            count += self.modified_merge_sort(nums, start, mid)
            count += self.modified_merge_sort(nums, mid + 1, end)
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
    result = solution.count_inversions_0([1, 20, 6, 4, 5])
    print(result)
    result = solution.count_inversions_1([1, 20, 6, 4, 5])
    print(result)
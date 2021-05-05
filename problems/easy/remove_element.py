'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''


class Solution:
    def remove_element(self, nums, val):
        occurance = 0
        index = 0
        while index < (len(nums) - occurance):
            if nums[index] == val:
                occurance += 1
                nums[index], nums[len(nums) -
                                  occurance] = nums[len(nums) -
                                                    occurance], nums[index]
            if nums[index] != val:
                index += 1
        return len(nums) - occurance


if __name__ == "__main__":
    solution = Solution()
    nums = [4, 5]
    result = solution.remove_element(nums, 5)
    print(result)
    print(nums)
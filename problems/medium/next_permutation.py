'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.
'''


def next_permutation(nums):
    shuffled = False
    for index in range(len(nums) - 1, 0, -1):
        for index2 in range(index - 1, -1, -1):
            if nums[index] > nums[index2]:
                nums[index], nums[index2] = nums[index2], nums[index]
                shuffled = True
                break
        if shuffled:
            break

    if not shuffled:
        i = 0
        for i in range(len(nums) // 2):
            nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i -
                                                    1], nums[i]


# nums = [3, 2, 1]
# nums = [1, 2, 3]
nums = [1, 3, 2]
result = next_permutation(nums)
print(nums)
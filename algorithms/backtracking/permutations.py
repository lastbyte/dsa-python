'''
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
'''

def generate_permutations(nums,left, right, permutations):

    if left == right:
        permutations.append(nums.copy())
    for i in range(left, right+1):
        nums[left], nums[i] = nums[i], nums[left]
        generate_permutations(nums, left+1, right, permutations)
        nums[left], nums[i] = nums[i], nums[left]


permutations = []
nums=[1,1,3]
generate_permutations(nums,0, len(nums)-1,permutations)
print(permutations)
